# Smishing Risk Assessment

## Repository Contents

| File | Description |
|---|---|
| `allowlist.csv` | 30 trusted Lithuanian domains (banks, government, postal/courier services, telecoms) used for domain allowlist verification. Columns: `company`, `domain`. |
| `shorteners-list.csv` | 657 known URL shortener domains used for URL shortener detection. Column: `domain`. |
| `reference-messages.csv` | 78 Lithuanian-language SMS messages (67 phishing, 11 benign) with precomputed 3 072-dimensional embeddings from OpenAI `text-embedding-3-large`. Columns: `message`, `scenario`, `vector_data`, `phishing`. |
| `raw-data.xlsx` | Raw evaluation results (risk scores, weights, reports) from the 600 LLM evaluation runs (20 messages x 3 models x 10 repetitions). |
| `data/` | 20 SMS screenshot images (10 phishing, 10 benign) used as evaluation inputs. |
| `system-prompt-template.txt` | LLM system prompt template for risk score generation (see Appendix A in the paper). |
| `screenshot-data-extraction-prompt.txt` | GPT-4o prompt used for OCR extraction from SMS screenshots. |

## Data Sources

- **Allowlist**: Manually curated by the authors based on Lithuanian domains most commonly impersonated in smishing campaigns.
- **Shortener list**: Aggregated from publicly available URL shortener domain compilations.
- **Reference messages**: Phishing examples collected from publicly shared Lithuanian smishing reports on social media and news sources, as well as from direct contributions by individuals who had received such messages. Benign examples drawn from authentic, non-malicious SMS messages. All messages were manually reviewed and labeled by the authors.
- **Phishing database**: The prototype checks URLs against [PhishTank](https://phishtank.org), a public community-driven phishing URL repository (not included in this repository).

## License

MIT
