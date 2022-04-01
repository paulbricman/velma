from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
from pathlib import Path


def negate(statement, candidates=2, contradiction_threshold=0.9, edit_threshold=3, lm=None, lm_tok=None, nli=None):
    assert statement and statement != '', 'Statement is empty.'

    if not lm:
        lm = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-1.3B')

    if not lm_tok:
        lm_tok = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')

    # if not nli:
    #     nli = pipeline('zero-shot-classification',
    #                    model='cross-encoder/nli-distilroberta-base')

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
    if completion_ids[-1] in [628, 198]:
        return [50256]
    return range(50256)
