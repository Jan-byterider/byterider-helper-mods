#!/bin/bash

# Convert Mermaid diagrams to images
mmdc -i pitch_deck_pitchDay_v2.md -o architecture.png
mmdc -i pitch_deck_pitchDay_v2.md -o security.png

# Generate PDF using pandoc
pandoc \
  pdf_config.yaml \
    \
  --from markdown \
  --to pdf \
  --pdf-engine=xelatex \
  --standalone \
  --toc \
  -o ByteNestDAO_Pitch_Deck.pdf

echo "PDF generated successfully!"