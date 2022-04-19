from transformers import AutoTokenizer, AutoModelForCausalLM
from src.util import softmax
import torch


def infer(context, statements, model=None, tokenizer=None, return_components=False):
    '''
    Infers which statement is most likely to follow from the context, normalized by statement likelihood.

    Args:
        context (str): Background context treated as premise in abduction.
        statements (list): List of statements to rank by likelihood.
        model (transformers.AutoModelForCausalLM): Language model to use.
        tokenizer (transformers.AutoTokenizer): Tokenizer to use.

    Returns:
        (list): List of probabilities of each statement.
    '''
    assert context and len(context) > 0, 'Empty context.'
    assert statements and isinstance(statements, list) and len(
        statements) == 2, 'Exactly two statements should be provided.'

    if not model:
        model = AutoModelForCausalLM.from_pretrained('distilgpt2')

    if not tokenizer:
        tokenizer = AutoTokenizer.from_pretrained('distilgpt2')

    priors = [lm_perplexity('', e, model, tokenizer) for e in statements]
    conditionals = [lm_perplexity(context, e, model, tokenizer)
                    for e in statements]
    probs = softmax([conditionals[0],
                    conditionals[1]], 0.2)
    if return_components:
        return {
            'priors': priors,
            'conditionals': conditionals
        }
    return probs


def lm_perplexity(prefix, completion, model=None, tokenizer=None):
    '''
    Computes the perplexity of a given completion given a prefix.

    Args:
        prefix (str): Prefix of the completion.
        completion (str): Completion to compute perplexity of.
        model (transformers.AutoModelForCausalLM): Language model to use.
        tokenizer (transformers.AutoTokenizer): Tokenizer to use.

    Returns:
        (float): Perplexity of the completion.
    '''
    assert completion and len(completion) > 0, 'Empty completion.'

    if not model:
        model = AutoModelForCausalLM.from_pretrained('distilgpt2')

    if not tokenizer:
        tokenizer = AutoTokenizer.from_pretrained('distilgpt2')

    completion_ids = tokenizer(completion, return_tensors='pt').input_ids
    completion_len = completion_ids.size(1)

    full = prefix + completion
    full_ids = tokenizer(full, return_tensors='pt').input_ids

    masked_full_ids = full_ids.clone()
    masked_full_ids[:, :-completion_len] = -100

    with torch.no_grad():
        output = model(full_ids, labels=masked_full_ids)
        neg_log_likelihood = -output[0]

    return float(neg_log_likelihood)
