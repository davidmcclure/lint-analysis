#!/bin/bash

VOCAB_FILE=$1
CORPUS_FILE=$2

CORPUS_NAME=$(basename $CORPUS_FILE .txt)
SAVE_FILE=$CORPUS_NAME.glove
SAVE_DIR=$(dirname "${SAVE_FILE}")
COOCCURRENCE_FILE=$SAVE_DIR/cooc.bin
COOCCURRENCE_SHUF_FILE=$SAVE_DIR/cooc.shuf.bin
BUILDDIR=$(dirname $0)/glove/build

MEMORY=6.0
VECTOR_SIZE=200
MAX_ITER=25
WINDOW_SIZE=15
BINARY=2
NUM_THREADS=8
X_MAX=10

$BUILDDIR/cooccur \
  -memory $MEMORY \
  -vocab-file $VOCAB_FILE \
  -window-size $WINDOW_SIZE \
  < $CORPUS_FILE \
  > $COOCCURRENCE_FILE

$BUILDDIR/shuffle \
  -memory $MEMORY \
  < $COOCCURRENCE_FILE \
  > $COOCCURRENCE_SHUF_FILE

$BUILDDIR/glove \
  -save-file $SAVE_FILE \
  -threads $NUM_THREADS \
  -input-file $COOCCURRENCE_SHUF_FILE \
  -iter $MAX_ITER \
  -vector-size $VECTOR_SIZE \
  -vocab-file $VOCAB_FILE

rm ${COOCCURRENCE_FILE} ${COOCCURRENCE_SHUF_FILE}

python -W ignore -m gensim.scripts.glove2word2vec \
  --input $SAVE_FILE.txt \
  --output $CORPUS_NAME.w2v.txt
