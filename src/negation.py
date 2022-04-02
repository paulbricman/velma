from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import CrossEncoder
from pathlib import Path
from textdistance import levenshtein


def gen_negations(statement, candidates=2, lm=None, lm_tok=None):
    '''
    Produce a list of candidates negations of a given statement.

    Args:
        statement (str): The statement to negate.
        candidates (int): The number of candidates to return.
        lm (str): The language model name.
        lm_tok (str): The language model tokenizer name.

    Returns:
        list: A list of candidates negations of the given statement.
    '''
    assert statement and statement != '', 'Statement is empty.'

    if not lm:
        lm = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-1.3B')

    if not lm_tok:
        lm_tok = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')

    prompt_path = Path('data') / 'negation_prompt.txt'
    if not prompt_path.exists():
        prompt_path = '..' / prompt_path

    prompt = open(prompt_path).read()
    prompt = f"{prompt} {statement}\nnegation:"
    prompt_ids = lm_tok(prompt, return_tensors='pt')['input_ids']
    prompt_size = prompt_ids.size(1)

    output = lm.generate(
        prompt_ids,
        output_scores=True,
        prefix_allowed_tokens_fn=lambda x, y: force_eos(y.tolist()),
        num_return_sequences=candidates,
        do_sample=True,
        max_length=prompt_size+30,
        min_length=prompt_size+3)

    output = [e[prompt_size:] for e in output]
    output = [[e for e in f if e != 50256] for f in output]
    output = lm_tok.batch_decode(output)
    output = [e.strip() for e in output]

    return output


def force_eos(completion_ids):
    '''
    Force text generation to stop after newline.

    Args:
        completion_ids (list): The list of previous token ids.

    Returns:
        list: The list of legal token ids.
    '''
    if completion_ids[-1] in [628, 198]:
        return [50256]
    return range(50256)


def filter_negations(statement, candidates, nli=None, lm_tok=None, nli_threshold=0.9, edit_threshold=3):
    '''
    Filter candidates to remove those that are not negations of the given statement. Also, encourage minimal edits.

    Args:
        candidates (list): A list of candidates to filter.
        statement (str): The statement to negate.
        nli (str): The NLI model name.

    Returns:
        list: A list of filtered candidates.
    '''
    assert statement and statement != '', 'Statement is empty.'

    if not nli:
        nli = CrossEncoder('cross-encoder/nli-deberta-v3-base')

    if not lm_tok:
        lm_tok = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')

    pairs = [(statement, e) for e in candidates]
    scores = nli.predict(pairs, apply_softmax=True)
    nli_filtered = [e for e_id, e in enumerate(
        candidates) if scores[e_id][0] > nli_threshold]

    # Batching would involve handling padding tokens properly...
    candidate_ids = [lm_tok(e, return_tensors='pt')['input_ids'][0].tolist()
                     for e in nli_filtered]
    statement_ids = lm_tok(statement, return_tensors='pt')[
        'input_ids'][0].tolist()
    edit_dists = [levenshtein.distance(statement_ids, e)
                  for e in candidate_ids]
    edit_filtered = [e for e_id, e in enumerate(
        nli_filtered) if edit_dists[e_id] <= edit_threshold]

    return edit_filtered
