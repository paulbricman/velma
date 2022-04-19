import streamlit as st
from src.abduction import infer
from src.baselines import infer_nli, infer_embs
from src.negation import filter_negations
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import AutoTokenizer, AutoModelForCausalLM


st.markdown('## ⚖️ velma')
st.info(
    'Read more about velma [here](https://paulbricman.com/thoughtware/velma).')


@st.cache(allow_output_mutation=True)
def load_models():
    emb_model = SentenceTransformer('all-MiniLM-L6-v2')
    nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')
    lm_model = AutoModelForCausalLM.from_pretrained(
        'distilgpt2')
    lm_tok = AutoTokenizer.from_pretrained('distilgpt2')
    return emb_model, nli_model, lm_model, lm_tok


emb_model, nli_model, lm_model, lm_tok = load_models()

st.markdown('---')
st.markdown('''When given a body of text and a pair of statements, velma will
    predict the one most likely to be compatible with the author\'s belief system.
    For instance, try using an extended bio of yours as context and a strong belief as P.
    Or perhaps a paper abstract as context and a claim as P.''')

context = st.text_area('context')
p = st.text_input('P')
not_p = st.text_input('¬P')


if st.button('start'):
    contradiction = filter_negations(
        p, [not_p], nli_model, lm_tok, edit_threshold=8, nli_threshold=0.8)
    if len(contradiction) == 0:
        st.error('P and ¬P are either not contradictory, or too syntactically different from each other. Try negating P with as few edits as possible.')
    else:
        with st.spinner('loading...'):
            velma = infer(context, [p, not_p], lm_model, lm_tok)
            embs = infer_embs(context, [p, not_p], emb_model)
            nli = infer_nli(context, [p, not_p],
                            nli=nli_model, mode='relative')

        st.markdown('')
        st.markdown('##### outputs (P vs ¬P)')
        st.markdown(f"velma (P={round(velma[0], 2)})")
        st.progress(velma[0])

        st.markdown(f'embs (P={round(embs[0], 2)})')
        st.progress(embs[0])

        st.markdown(f'nli (P={round(nli[0], 2)})')
        st.progress(float(nli[0]))
