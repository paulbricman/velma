from src.abduction import lm_perplexity, infer
from transformers import AutoTokenizer, AutoModelForCausalLM


def test_lm_perplexity():
    model = AutoModelForCausalLM.from_pretrained('distilgpt2')
    tokenizer = AutoTokenizer.from_pretrained('distilgpt2')

    assert lm_perplexity('Two plus two is', ' four', model, tokenizer) > \
        lm_perplexity('Two plus two is', ' hotdog', model, tokenizer)


def test_infer():
    model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-1.3B')
    tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')

    context = 'Social media is awesome because it allows you to connect with others.'
    statements = [' Facebook is amazing.',
                  ' Facebook is awful.']

    probs = infer(context, statements, model, tokenizer)
    assert probs[0] > probs[1], statements

    context = 'Being vegan is the way to go. Let\'s save the planet.'
    statements = [' Eating meat is completely ethical.',
                  ' Eating meat is not ethical.']

    probs = infer(context, statements, model, tokenizer)
    assert probs[1] > probs[0], statements
