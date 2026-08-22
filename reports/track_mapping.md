# トラック正規化の判定一覧

DBLP の目次見出し（`<h2>`）ごとに、どのルールでどのトラック種別に
判定されたかを全件示す。`config/tracks.yaml` のルールを検証するための資料。

- `full`: 主研究トラックのフル論文（**本サーベイの集計対象**）
- `short`: 短編・ポスター論文
- `industry`: 産業界トラックのフル長論文（主集計外・別途参照用）
- `other_track`: Resource / Reproducibility / Dataset など別枠の査読トラック（主集計外）
- `excluded`: デモ・チュートリアル・招待講演・Doctoral Symposium 等

## 種別ごとの件数

| track_class   |    n |
|:--------------|-----:|
| full          | 8893 |
| excluded      | 2677 |
| short         | 2475 |
| industry      | 1555 |
| other_track   |  487 |

## 会議 × 年 × 見出しの判定結果

| venue   |   year | track_heading                                                                       | track_class   | track_rule                   |   n |   median_pages |
|:--------|-------:|:------------------------------------------------------------------------------------|:--------------|:-----------------------------|----:|---------------:|
| CIKM    |   2019 | Demo - Demo Session 1                                                               | excluded      | heading:excluded             |  13 |            4   |
| CIKM    |   2019 | Demo - Demo Session 2                                                               | excluded      | heading:excluded             |  12 |            4   |
| CIKM    |   2019 | Tutorials                                                                           | excluded      | heading:excluded             |   9 |            2   |
| CIKM    |   2019 | Workshop Summaries                                                                  | excluded      | heading:excluded             |   9 |            2   |
| CIKM    |   2019 | Keynote Address                                                                     | excluded      | heading:excluded             |   4 |            1   |
| CIKM    |   2019 | Applied - Novel Applications                                                        | full          | pages:full                   |   6 |            9   |
| CIKM    |   2019 | Applied - Online and User bahaviors                                                 | full          | pages:full                   |   6 |            9   |
| CIKM    |   2019 | Applied - Recommendation and Advertising                                            | full          | pages:full                   |   6 |            9   |
| CIKM    |   2019 | Applied - Graph Applications                                                        | full          | pages:full                   |   5 |            9   |
| CIKM    |   2019 | Long - Algorithmic Techniques                                                       | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Analyzing Spatio-Temporal Data                                               | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Biomedical Informatics                                                       | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Computer Vision                                                              | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Deep Nerual Network I                                                        | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Domain Adaptation and Transfer Learning                                      | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - E-Commerce and Advertising I                                                 | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - E-Commerce and Advertising II                                                | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Graph Nerual Network I                                                       | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Graph Nerual Network II                                                      | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Knowledge Graph I                                                            | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Knowledge Graph II                                                           | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Machine Learning Themes I                                                    | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Machine Learning Themes II                                                   | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Mining in Emerging Applications II                                           | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Natural Language Processing I                                                | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Natural Language Processing II                                               | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Network Embedding I                                                          | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Network Embedding II                                                         | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Network Science                                                              | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Online and Real-Time                                                         | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Privacy                                                                      | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Question Answering and Dialogue Systems I                                    | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Question Answering and Dialogue Systems II                                   | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Recommendation System I                                                      | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Recommendation System II                                                     | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Recommendation System III                                                    | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Reinforcement Learning                                                       | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Search & Retrieval                                                           | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Sequential Data Analysis                                                     | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Understanding and Interpretability I                                         | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Understanding and Interpretability II                                        | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Urban Computing I                                                            | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - Urban Computing II                                                           | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Long - User Behavior                                                                | full          | heading:full                 |   5 |           10   |
| CIKM    |   2019 | Applied - E-commerce                                                                | full          | pages:full                   |   4 |            9   |
| CIKM    |   2019 | Applied - Language Models                                                           | full          | pages:full                   |   4 |            9   |
| CIKM    |   2019 | Applied - Urbanism and Mobility                                                     | full          | pages:full                   |   4 |            9   |
| CIKM    |   2019 | Long - Database and System                                                          | full          | heading:full                 |   4 |           10   |
| CIKM    |   2019 | Long - Deep Nerual Network II                                                       | full          | heading:full                 |   4 |           10   |
| CIKM    |   2019 | Long - Heterogeneous Data                                                           | full          | heading:full                 |   4 |           10   |
| CIKM    |   2019 | Long - Machine Learning Themes III                                                  | full          | heading:full                 |   4 |           10   |
| CIKM    |   2019 | Long - Mining in Emerging Applications I                                            | full          | heading:full                 |   4 |           10   |
| CIKM    |   2019 | Long - Social Network                                                               | full          | heading:full                 |   4 |           10   |
| CIKM    |   2019 | Short - Algorithm                                                                   | short         | heading:short                |   7 |            4   |
| CIKM    |   2019 | Short - Anomaly Detection                                                           | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Classification                                                              | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - E-commerce & Production                                                     | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Embeddings                                                                  | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Graph Neural Networks                                                       | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Information Retrieval                                                       | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Machine Learning                                                            | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Recognition                                                                 | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Recommendation                                                              | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Search                                                                      | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - System & Database                                                           | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Theory                                                                      | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Time Sequences & Dynamics                                                   | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Urbanism and Mobility                                                       | short         | heading:short                |   6 |            4   |
| CIKM    |   2019 | Short - Health & Sentiment                                                          | short         | heading:short                |   5 |            4   |
| CIKM    |   2019 | Short - Interpretability & Reasoning                                                | short         | heading:short                |   5 |            4   |
| CIKM    |   2019 | Short - Knowledge Extraction & Generation                                           | short         | heading:short                |   5 |            4   |
| CIKM    |   2019 | Applied - E-commerce                                                                | short         | pages:short                  |   1 |            7   |
| CIKM    |   2019 | Applied - Online and User bahaviors                                                 | short         | pages:short                  |   1 |            7   |
| CIKM    |   2019 | Applied - Urbanism and Mobility                                                     | short         | pages:short                  |   1 |            7   |
| CIKM    |   2020 | Demonstrations                                                                      | excluded      | heading:excluded             |  35 |            4   |
| CIKM    |   2020 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  12 |            4   |
| CIKM    |   2020 | Tutorials                                                                           | excluded      | heading:excluded             |  11 |            2   |
| CIKM    |   2020 | Workshop Summaries                                                                  | excluded      | heading:excluded             |   9 |            2   |
| CIKM    |   2020 | Keynote Talks                                                                       | excluded      | heading:excluded             |   2 |            1   |
| CIKM    |   2020 | Full Paper Track                                                                    | full          | heading:full                 | 193 |           10   |
| CIKM    |   2020 | Applied Research Track                                                              | industry      | heading:industry             |  73 |            8   |
| CIKM    |   2020 | Resource Track                                                                      | other_track   | heading:other_track          |  32 |            8   |
| CIKM    |   2020 | Short Paper Track                                                                   | short         | heading:short                | 102 |            4   |
| CIKM    |   2020 | Poster Presentations                                                                | short         | pages:short                  |  25 |            4   |
| CIKM    |   2021 | Demo Papers                                                                         | excluded      | heading:excluded             |  35 |            5   |
| CIKM    |   2021 | Tutorials                                                                           | excluded      | heading:excluded             |   9 |            4   |
| CIKM    |   2021 | Workshops                                                                           | excluded      | heading:excluded             |   9 |            2   |
| CIKM    |   2021 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| CIKM    |   2021 | Full Paper Track                                                                    | full          | heading:full                 | 271 |           10   |
| CIKM    |   2021 | Applied Research Paper Track                                                        | industry      | heading:industry             |  70 |           10   |
| CIKM    |   2021 | Resource Paper Track                                                                | other_track   | heading:other_track          |  25 |           10   |
| CIKM    |   2021 | Short Paper Track                                                                   | short         | heading:short                | 177 |            5   |
| CIKM    |   2022 | CIKM'22 Demonstrations                                                              | excluded      | heading:excluded             |  56 |            5   |
| CIKM    |   2022 | CIKM'22 Industry Day Talks                                                          | excluded      | heading:excluded             |  13 |            2   |
| CIKM    |   2022 | CIKM'22 Workshops                                                                   | excluded      | heading:excluded             |  11 |            2   |
| CIKM    |   2022 | CIKM'22 PhD Symposium                                                               | excluded      | heading:excluded             |   7 |            4   |
| CIKM    |   2022 | CIKM'22 Tutorials                                                                   | excluded      | heading:excluded             |   7 |            4   |
| CIKM    |   2022 | Keynote Talks                                                                       | excluded      | heading:excluded             |   4 |            1   |
| CIKM    |   2022 | CIKM'22 Full Papers                                                                 | full          | heading:full                 | 272 |           10   |
| CIKM    |   2022 | CIKM'22 Applied Research Papers                                                     | industry      | heading:industry             |  90 |           10   |
| CIKM    |   2022 | CIKM'22 Short Papers                                                                | short         | heading:short                | 195 |            5   |
| CIKM    |   2023 | Applied Research Papers                                                             | excluded      | heading:industry+pages:short |  62 |            7   |
| CIKM    |   2023 | Demo Papers                                                                         | excluded      | heading:excluded             |  26 |            5   |
| CIKM    |   2023 | Workshop Proposals                                                                  | excluded      | heading:excluded             |  15 |            4   |
| CIKM    |   2023 | Industry Day                                                                        | excluded      | heading:industry+pages:short |  14 |            2   |
| CIKM    |   2023 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |   9 |            4   |
| CIKM    |   2023 | Tutorial Proposals                                                                  | excluded      | heading:excluded             |   9 |            4   |
| CIKM    |   2023 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| CIKM    |   2023 | Full Papers                                                                         | full          | heading:full                 | 354 |           10   |
| CIKM    |   2023 | Applied Research Papers                                                             | industry      | heading:industry             |  11 |            8   |
| CIKM    |   2023 | Resource Papers                                                                     | other_track   | heading:other_track          |  22 |            5   |
| CIKM    |   2023 | Short Papers                                                                        | short         | heading:short                | 151 |            5   |
| CIKM    |   2024 | Demo Papers                                                                         | excluded      | heading:excluded             |  33 |            5   |
| CIKM    |   2024 | PhD Symposium                                                                       | excluded      | heading:excluded             |  19 |            4   |
| CIKM    |   2024 | Tutorial Presentations                                                              | excluded      | heading:excluded             |  12 |            4   |
| CIKM    |   2024 | Industry Day Talks                                                                  | excluded      | heading:excluded             |  10 |            2   |
| CIKM    |   2024 | Workshops                                                                           | excluded      | heading:excluded             |  10 |            3.5 |
| CIKM    |   2024 | Applied Research Papers                                                             | excluded      | heading:industry+pages:short |   5 |            7   |
| CIKM    |   2024 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| CIKM    |   2024 | Full Research Papers                                                                | full          | heading:full                 | 345 |           10   |
| CIKM    |   2024 | Applied Research Papers                                                             | industry      | heading:industry             |  96 |            8   |
| CIKM    |   2024 | Resource Papers                                                                     | other_track   | heading:other_track          |  21 |            5   |
| CIKM    |   2024 | Short Research Papers                                                               | short         | heading:short                | 139 |            5   |
| CIKM    |   2025 | Demo Papers                                                                         | excluded      | heading:excluded             |  36 |            5   |
| CIKM    |   2025 | Workshops                                                                           | excluded      | heading:excluded             |  14 |            4   |
| CIKM    |   2025 | Industry Day Talks                                                                  | excluded      | heading:excluded             |  13 |            2   |
| CIKM    |   2025 | PhD Symposium                                                                       | excluded      | heading:excluded             |  11 |            4   |
| CIKM    |   2025 | Tutorials                                                                           | excluded      | heading:excluded             |  10 |            4   |
| CIKM    |   2025 | Applied Research Papers                                                             | excluded      | heading:industry+pages:short |   3 |            7   |
| CIKM    |   2025 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| CIKM    |   2025 | Full Research Papers                                                                | full          | heading:full                 | 433 |           10   |
| CIKM    |   2025 | Applied Research Papers                                                             | industry      | heading:industry             |  89 |            8   |
| CIKM    |   2025 | Resource Papers                                                                     | other_track   | heading:other_track          |  51 |            5   |
| CIKM    |   2025 | Short Research Papers                                                               | short         | heading:short                | 183 |            5   |
| KDD     |   2019 | Tutorials                                                                           | excluded      | heading:excluded             |  29 |            2   |
| KDD     |   2019 | Applied Data Science Invited Talks                                                  | excluded      | heading:excluded             |  22 |            1   |
| KDD     |   2019 | Keynote Talks                                                                       | excluded      | heading:excluded             |   2 |            2   |
| KDD     |   2019 | Research Track Papers                                                               | full          | heading:full                 | 174 |           10   |
| KDD     |   2019 | Applied Data Science Track Papers                                                   | industry      | heading:industry             | 147 |            9   |
| KDD     |   2020 | Tutorial Abstracts                                                                  | excluded      | heading:excluded             |  44 |            2   |
| KDD     |   2020 | Diversity and Inclusion Abstracts                                                   | excluded      | heading:excluded             |  14 |            1   |
| KDD     |   2020 | Applied Data Science Invited Talks Abstracts                                        | excluded      | heading:excluded             |  12 |            1   |
| KDD     |   2020 | Keynote & Invited Talks                                                             | excluded      | heading:excluded             |   4 |            1   |
| KDD     |   2020 | Panel                                                                               | excluded      | heading:excluded             |   1 |            2   |
| KDD     |   2020 | Research Track Papers                                                               | full          | heading:full                 | 217 |           10   |
| KDD     |   2020 | Applied Data Science Track Papers                                                   | industry      | heading:industry             | 121 |            9   |
| KDD     |   2020 | Health Day Papers                                                                   | other_track   | heading:other_track          |   8 |            8   |
| KDD     |   2021 | Workshop Summaries                                                                  | excluded      | heading:excluded             |  44 |            2   |
| KDD     |   2021 | Tutorial Overviews                                                                  | excluded      | heading:excluded             |  40 |            2   |
| KDD     |   2021 | Keynote Talks                                                                       | excluded      | heading:excluded             |   4 |            1   |
| KDD     |   2021 | ADS Track Papers                                                                    | excluded      | heading:industry+pages:short |   1 |            7   |
| KDD     |   2021 | Research Track Papers                                                               | full          | heading:full                 | 239 |           11   |
| KDD     |   2021 | ADS Track Papers                                                                    | industry      | heading:industry             | 154 |           10   |
| KDD     |   2022 | Tutorial Overviews                                                                  | excluded      | heading:excluded             |  39 |            2   |
| KDD     |   2022 | Workshop Summaries                                                                  | excluded      | heading:excluded             |  33 |            2   |
| KDD     |   2022 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| KDD     |   2022 | Research Track Full Papers                                                          | full          | heading:full                 | 253 |           11   |
| KDD     |   2022 | ADS Track Papers                                                                    | industry      | heading:industry             | 196 |           10   |
| KDD     |   2022 | Health Day Papers                                                                   | other_track   | heading:other_track          |  10 |            9   |
| KDD     |   2023 | Workshop Summaries                                                                  | excluded      | heading:excluded             |  34 |            2   |
| KDD     |   2023 | Lecture Style Tutorials                                                             | excluded      | heading:excluded             |  27 |            2   |
| KDD     |   2023 | Hands On Tutorials                                                                  | excluded      | heading:excluded             |   7 |            2   |
| KDD     |   2023 | Research Track Full Papers                                                          | full          | heading:full                 | 313 |           12   |
| KDD     |   2023 | Applied Data Track Full Papers                                                      | industry      | heading:industry             | 183 |           11   |
| KDD     |   2024 | Workshop Summaries                                                                  | excluded      | heading:excluded             |  30 |            2   |
| KDD     |   2024 | Lecture-Style Tutorials                                                             | excluded      | heading:excluded             |  25 |           11   |
| KDD     |   2024 | Hands-On Tutorials                                                                  | excluded      | heading:excluded             |   9 |            2   |
| KDD     |   2024 | Special Day Abstracts                                                               | excluded      | heading:excluded             |   8 |            2   |
| KDD     |   2024 | Applied Data Invited Talks                                                          | excluded      | heading:excluded             |   5 |            1   |
| KDD     |   2024 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| KDD     |   2024 | Research Track Papers                                                               | full          | heading:full                 | 410 |           12   |
| KDD     |   2024 | Applied Data Papers                                                                 | industry      | heading:industry             | 151 |           11   |
| KDD     |   2025 | Workshop Summaries                                                                  | excluded      | heading:excluded             |  29 |            2   |
| KDD     |   2025 | Lecture Style Tutorials                                                             | excluded      | heading:excluded             |  23 |           11   |
| KDD     |   2025 | Hands-on Tutorials                                                                  | excluded      | heading:excluded             |   8 |            2   |
| KDD     |   2025 | Special Day Talks                                                                   | excluded      | heading:excluded             |   5 |            2   |
| KDD     |   2025 | Applied Data Invited Talks                                                          | excluded      | heading:excluded             |   4 |            1   |
| KDD     |   2025 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| KDD     |   2025 | Panel                                                                               | excluded      | heading:excluded             |   1 |            1   |
| KDD     |   2025 | Research Track                                                                      | full          | heading:full                 | 551 |           12   |
| KDD     |   2025 | Applied Data Track                                                                  | industry      | heading:industry             |  91 |           11   |
| KDD     |   2025 | Applied Data Science Track                                                          | industry      | heading:industry             |  62 |           11   |
| KDD     |   2025 | Dataset/Benchmark Track                                                             | other_track   | heading:other_track          |  62 |           12   |
| RecSys  |   2019 | Workshops, challenge, and late-breaking results                                     | excluded      | heading:excluded             |  13 |            2   |
| RecSys  |   2019 | Demonstrations                                                                      | excluded      | heading:excluded             |   7 |            2   |
| RecSys  |   2019 | Doctoral symposium                                                                  | excluded      | heading:excluded             |   6 |            5   |
| RecSys  |   2019 | Tutorials                                                                           | excluded      | heading:excluded             |   6 |            2   |
| RecSys  |   2019 | Invited keynotes                                                                    | excluded      | heading:excluded             |   2 |            1   |
| RecSys  |   2019 | Algorithms: Large-scale, constraints and evaluation                                 | full          | pages:full                   |   6 |            9   |
| RecSys  |   2019 | Application of recommenders in personal needs                                       | full          | pages:full                   |   5 |            9   |
| RecSys  |   2019 | Deep learning for recommender systems                                               | full          | pages:full                   |   5 |            9   |
| RecSys  |   2019 | Ranking and deep learning in recommenders                                           | full          | pages:full                   |   5 |            9   |
| RecSys  |   2019 | Recommendation in advertising, promotions, intent and search                        | full          | pages:full                   |   5 |            9   |
| RecSys  |   2019 | User side of recommender systems                                                    | full          | pages:full                   |   5 |            9   |
| RecSys  |   2019 | Using side-information and user attributes and cold-start in recommender algorithms | full          | pages:full                   |   5 |            9   |
| RecSys  |   2019 | Short papers with poster presentation                                               | short         | heading:short                |  34 |            5   |
| RecSys  |   2019 | Novel approaches to recommenders                                                    | short         | pages:short                  |   6 |            1   |
| RecSys  |   2019 | Novel uses of recommenders                                                          | short         | pages:short                  |   5 |            1   |
| RecSys  |   2019 | Application of recommenders in personal needs                                       | short         | pages:short                  |   1 |            5   |
| RecSys  |   2019 | Deep learning for recommender systems                                               | short         | pages:short                  |   1 |            5   |
| RecSys  |   2019 | Ranking and deep learning in recommenders                                           | short         | pages:short                  |   1 |            5   |
| RecSys  |   2019 | Recommendation in advertising, promotions, intent and search                        | short         | pages:short                  |   1 |            5   |
| RecSys  |   2019 | User side of recommender systems                                                    | short         | pages:short                  |   1 |            5   |
| RecSys  |   2019 | Using side-information and user attributes and cold-start in recommender algorithms | short         | pages:short                  |   1 |            5   |
| RecSys  |   2020 | Late-Breaking Results                                                               | excluded      | heading:excluded             |  17 |            6   |
| RecSys  |   2020 | Workshops & Challenge                                                               | excluded      | heading:excluded             |  12 |            2   |
| RecSys  |   2020 | Industry Papers                                                                     | excluded      | heading:industry+pages:short |  10 |            2   |
| RecSys  |   2020 | Demonstrations                                                                      | excluded      | heading:excluded             |   9 |            3   |
| RecSys  |   2020 | Doctoral Symposium                                                                  | excluded      | heading:excluded             |   8 |            5.5 |
| RecSys  |   2020 | Tutorials                                                                           | excluded      | heading:excluded             |   6 |            3   |
| RecSys  |   2020 | Invited Keynotes                                                                    | excluded      | heading:excluded             |   3 |            1   |
| RecSys  |   2020 | Long Papers                                                                         | full          | heading:full                 |  41 |           10   |
| RecSys  |   2020 | Short Papers                                                                        | short         | heading:short                |  26 |            6   |
| RecSys  |   2021 | Industry Papers                                                                     | excluded      | heading:industry+pages:short |  25 |            3   |
| RecSys  |   2021 | Late-breaking Results                                                               | excluded      | heading:excluded             |  24 |            6   |
| RecSys  |   2021 | Workshops and Challenge                                                             | excluded      | heading:excluded             |  18 |            3   |
| RecSys  |   2021 | Demonstrations                                                                      | excluded      | heading:excluded             |   8 |            4   |
| RecSys  |   2021 | Doctoral Symposium                                                                  | excluded      | heading:excluded             |   8 |            5   |
| RecSys  |   2021 | Tutorials                                                                           | excluded      | heading:excluded             |   6 |            3   |
| RecSys  |   2021 | Language and Knowledge                                                              | full          | pages:full                   |   6 |           11   |
| RecSys  |   2021 | Real-World Concerns                                                                 | full          | pages:full                   |   6 |           10   |
| RecSys  |   2021 | Algorithmic Advances                                                                | full          | pages:full                   |   4 |           10   |
| RecSys  |   2021 | Applications-Driven Advances                                                        | full          | pages:full                   |   4 |           10   |
| RecSys  |   2021 | Interactive Recommendation                                                          | full          | pages:full                   |   4 |           11   |
| RecSys  |   2021 | Metrics and Evaluation                                                              | full          | pages:full                   |   4 |           10.5 |
| RecSys  |   2021 | Practical Issues                                                                    | full          | pages:full                   |   4 |           11   |
| RecSys  |   2021 | Privacy, Fairness, Bias                                                             | full          | pages:full                   |   4 |           10   |
| RecSys  |   2021 | Theory and Practice                                                                 | full          | pages:full                   |   4 |           10.5 |
| RecSys  |   2021 | Echo Chambers and Filter Bubbles                                                    | full          | pages:full                   |   3 |           11   |
| RecSys  |   2021 | Scalable Performance                                                                | full          | pages:full                   |   3 |           10   |
| RecSys  |   2021 | Users in Focus                                                                      | full          | pages:full                   |   2 |            9.5 |
| RecSys  |   2021 | Reproducibility Papers                                                              | other_track   | heading:other_track          |   3 |            9   |
| RecSys  |   2021 | Metrics and Evaluation                                                              | short         | pages:short                  |   1 |            6   |
| RecSys  |   2022 | Industry Papers                                                                     | excluded      | heading:industry+pages:short |  30 |            3   |
| RecSys  |   2022 | Workshops and Challenge                                                             | excluded      | heading:excluded             |  15 |            3   |
| RecSys  |   2022 | Late-Breaking Results                                                               | excluded      | heading:excluded             |  13 |            6   |
| RecSys  |   2022 | Doctoral Symposium                                                                  | excluded      | heading:excluded             |   9 |            2   |
| RecSys  |   2022 | Tutorials                                                                           | excluded      | heading:excluded             |   8 |            2   |
| RecSys  |   2022 | Demonstrations                                                                      | excluded      | heading:excluded             |   6 |            4   |
| RecSys  |   2022 | Keynotes                                                                            | excluded      | heading:excluded             |   2 |            1   |
| RecSys  |   2022 | Models and Learning I                                                               | full          | pages:full                   |   7 |           11   |
| RecSys  |   2022 | Diversity and Novelty                                                               | full          | pages:full                   |   5 |           10   |
| RecSys  |   2022 | Models and Learning II                                                              | full          | pages:full                   |   5 |           10   |
| RecSys  |   2022 | Sequential Recommendation                                                           | full          | pages:full                   |   5 |           10   |
| RecSys  |   2022 | Domain-Specific Recommendation                                                      | full          | pages:full                   |   4 |           11   |
| RecSys  |   2022 | Fairness and Privacy                                                                | full          | pages:full                   |   4 |           11   |
| RecSys  |   2022 | User Modeling                                                                       | full          | pages:full                   |   4 |           11   |
| RecSys  |   2022 | Sessions and Interaction                                                            | full          | pages:full                   |   3 |           11   |
| RecSys  |   2022 | Large-Scale Recommendation                                                          | full          | pages:full                   |   2 |           10.5 |
| RecSys  |   2022 | Reproducibility Papers                                                              | other_track   | heading:other_track          |   3 |            9   |
| RecSys  |   2023 | Late-Breaking Results                                                               | excluded      | heading:excluded             |  20 |            6   |
| RecSys  |   2023 | Workshops and Challenge                                                             | excluded      | heading:excluded             |  19 |            4   |
| RecSys  |   2023 | Industry Posters                                                                    | excluded      | heading:industry+pages:short |  16 |            4   |
| RecSys  |   2023 | Doctoral Symposium                                                                  | excluded      | heading:excluded             |  15 |            5   |
| RecSys  |   2023 | Tutorials                                                                           | excluded      | heading:excluded             |   6 |            2   |
| RecSys  |   2023 | Demonstrations                                                                      | excluded      | heading:excluded             |   5 |            4   |
| RecSys  |   2023 | Sequential Recommendation                                                           | full          | pages:full                   |   7 |           11   |
| RecSys  |   2023 | Collaborative filtering                                                             | full          | pages:full                   |   6 |           11   |
| RecSys  |   2023 | Interactive Recommendation                                                          | full          | pages:full                   |   5 |           12   |
| RecSys  |   2023 | Applications                                                                        | full          | pages:full                   |   4 |           11.5 |
| RecSys  |   2023 | Cross-domain Recommendation                                                         | full          | pages:full                   |   4 |           12.5 |
| RecSys  |   2023 | Reinforcement Learning                                                              | full          | pages:full                   |   4 |           12   |
| RecSys  |   2023 | Trustworthy Recommendation                                                          | full          | pages:full                   |   4 |           11   |
| RecSys  |   2023 | Click-Through Rate Prediction                                                       | full          | pages:full                   |   3 |           12   |
| RecSys  |   2023 | Graphs                                                                              | full          | pages:full                   |   3 |           12   |
| RecSys  |   2023 | Knowledge and Context                                                               | full          | pages:full                   |   3 |           11   |
| RecSys  |   2023 | Multi-task Recommendation                                                           | full          | pages:full                   |   3 |           12   |
| RecSys  |   2023 | Multimedia Recommendation                                                           | full          | pages:full                   |   3 |           11   |
| RecSys  |   2023 | Evaluation                                                                          | full          | pages:full                   |   2 |           12.5 |
| RecSys  |   2023 | Side Information, Items structure and Relations                                     | full          | pages:full                   |   2 |           11.5 |
| RecSys  |   2023 | Short Papers                                                                        | short         | heading:short                |  48 |            7   |
| RecSys  |   2023 | Interactive Recommendation                                                          | short         | pages:short                  |   3 |            4   |
| RecSys  |   2023 | Collaborative filtering                                                             | short         | pages:short                  |   2 |            4.5 |
| RecSys  |   2023 | Evaluation                                                                          | short         | pages:short                  |   2 |            5   |
| RecSys  |   2023 | Side Information, Items structure and Relations                                     | short         | pages:short                  |   2 |            2.5 |
| RecSys  |   2023 | Click-Through Rate Prediction                                                       | short         | pages:short                  |   1 |            5   |
| RecSys  |   2023 | Graphs                                                                              | short         | pages:short                  |   1 |            4   |
| RecSys  |   2023 | Knowledge and Context                                                               | short         | pages:short                  |   1 |            3   |
| RecSys  |   2023 | Multi-task Recommendation                                                           | short         | pages:short                  |   1 |            3   |
| RecSys  |   2023 | Multimedia Recommendation                                                           | short         | pages:short                  |   1 |            3   |
| RecSys  |   2023 | Sequential Recommendation                                                           | short         | pages:short                  |   1 |            4   |
| RecSys  |   2024 | Industry track                                                                      | excluded      | heading:industry+pages:short |  34 |            3   |
| RecSys  |   2024 | Doctoral symposium                                                                  | excluded      | heading:excluded             |  21 |            6   |
| RecSys  |   2024 | Workshops and Challenge                                                             | excluded      | heading:excluded             |  21 |            3   |
| RecSys  |   2024 | Late-breaking results                                                               | excluded      | heading:excluded             |  18 |            6   |
| RecSys  |   2024 | Demonstrations                                                                      | excluded      | heading:excluded             |   6 |            3.5 |
| RecSys  |   2024 | Tutorials                                                                           | excluded      | heading:excluded             |   6 |            2   |
| RecSys  |   2024 | Large language models                                                               | full          | pages:full                   |  12 |           10   |
| RecSys  |   2024 | Optimisation and evaluation                                                         | full          | pages:full                   |  10 |           10   |
| RecSys  |   2024 | Bias and fairness                                                                   | full          | pages:full                   |   9 |           10   |
| RecSys  |   2024 | Sequential recommendation                                                           | full          | pages:full                   |   9 |           11   |
| RecSys  |   2024 | Collaborative filtering                                                             | full          | pages:full                   |   6 |           10   |
| RecSys  |   2024 | Cold-start                                                                          | full          | pages:full                   |   5 |           10   |
| RecSys  |   2024 | Cross-domain and cross-modal learning                                               | full          | pages:full                   |   5 |           11   |
| RecSys  |   2024 | Graph learning                                                                      | full          | pages:full                   |   4 |           10.5 |
| RecSys  |   2024 | Multi-task learning                                                                 | full          | pages:full                   |   4 |           10   |
| RecSys  |   2024 | Robust recommender systems                                                          | full          | pages:full                   |   4 |           10.5 |
| RecSys  |   2024 | Off-policy learning                                                                 | full          | pages:full                   |   3 |           10   |
| RecSys  |   2024 | Short papers                                                                        | short         | heading:short                |  39 |            6   |
| RecSys  |   2024 | Optimisation and evaluation                                                         | short         | pages:short                  |   1 |            6   |
| RecSys  |   2025 | Industry track                                                                      | excluded      | heading:industry+pages:short |  54 |            4   |
| RecSys  |   2025 | Late-breaking Results                                                               | excluded      | heading:excluded             |  34 |            6   |
| RecSys  |   2025 | Workshops and Challenge                                                             | excluded      | heading:excluded             |  15 |            4   |
| RecSys  |   2025 | Doctoral Symposium                                                                  | excluded      | heading:excluded             |  12 |            6   |
| RecSys  |   2025 | Demonstrations                                                                      | excluded      | heading:excluded             |  11 |            3   |
| RecSys  |   2025 | Tutorials                                                                           | excluded      | heading:excluded             |   8 |            3   |
| RecSys  |   2025 | Full papers                                                                         | full          | heading:full                 |  48 |           10   |
| RecSys  |   2025 | Reproducibility Papers                                                              | other_track   | heading:other_track          |  22 |           10   |
| RecSys  |   2025 | Short Papers                                                                        | short         | heading:short                |  33 |            6   |
| SIGIR   |   2019 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  14 |            1   |
| SIGIR   |   2019 | Tutorials                                                                           | excluded      | heading:excluded             |  11 |            2   |
| SIGIR   |   2019 | Workshops                                                                           | excluded      | heading:excluded             |   8 |            3   |
| SIGIR   |   2019 | Demonstration Papers 1: Interactive IR Systems                                      | excluded      | heading:excluded             |   7 |            4   |
| SIGIR   |   2019 | Demonstration Papers 2: Evaluation & Entities                                       | excluded      | heading:excluded             |   7 |            4   |
| SIGIR   |   2019 | Demonstration Papers 3: Applications                                                | excluded      | heading:excluded             |   7 |            4   |
| SIGIR   |   2019 | SIRIP 1: Voice, Entertainment, and Suggestions                                      | excluded      | heading:industry+pages:short |   4 |            2   |
| SIGIR   |   2019 | SIRIP 2: Recommendation, Search, and Advertising                                    | excluded      | heading:industry+pages:short |   4 |            2   |
| SIGIR   |   2019 | SIRIP 3: Various Applications                                                       | excluded      | heading:industry+pages:short |   3 |            2   |
| SIGIR   |   2019 | SIRIP 4: Legal IR                                                                   | excluded      | heading:industry+pages:short |   3 |            2   |
| SIGIR   |   2019 | Keynote & Invited Talks                                                             | excluded      | heading:excluded             |   2 |            2   |
| SIGIR   |   2019 | Session 2A: Question Answering                                                      | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2019 | Session 2B: Collaborative Filtering                                                 | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2019 | Session 2C: Knowledge and Entities                                                  | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2019 | Session 5A: Conversation and Dialog                                                 | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2019 | Session 3A: Recommendations 1                                                       | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 3B: Interpretatibility and Explainability                                   | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 3C: Fact-checking, Privacy and Legal                                        | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 6A: Social Media                                                            | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 6B: Personalization and Personal Data Search                                | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 7A: Relevance and Evaluation 1                                              | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 7C: Recommendations 2                                                       | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2019 | Session 1A: Learning to Rank 1                                                      | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 1B: Health and Social Media                                                 | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 4A: Recommendations and Classificatiion                                     | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 4B: Queries                                                                 | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 4C: Users and Tasks                                                         | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 5B: Efficiency, Effectiveness and Performance                               | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 7B: Multilingual and Cross-modal Retrieval                                  | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 8B: Hashing                                                                 | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 9A: Fashion Match                                                           | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 9B: Relevance and Evaluation 2                                              | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2019 | Session 8C: Summarization and Information Extraction                                | full          | pages:full                   |   2 |           10   |
| SIGIR   |   2019 | Session 9C: Learning to Rank 2                                                      | full          | pages:full                   |   2 |           10   |
| SIGIR   |   2019 | Session 1C: Search Intents                                                          | full          | pages:full                   |   1 |           10   |
| SIGIR   |   2019 | Session 8A: User Behavior and Experience                                            | full          | pages:full                   |   1 |           10   |
| SIGIR   |   2019 | Short Research Papers 1A: AI, Mining, and Others                                    | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 1B: Recommendation and Evaluation                             | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 1C: Search                                                    | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 2A: AI, Mining, and Others                                    | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 2B: Recommendation and Evaluation                             | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 2C: Search                                                    | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 3A: AI, Mining, and Others                                    | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 3B: Recommendation and Evaluation                             | short         | heading:short                |  12 |            4   |
| SIGIR   |   2019 | Short Research Papers 3C: Search                                                    | short         | heading:short                |  12 |            4   |
| SIGIR   |   2020 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  14 |            1   |
| SIGIR   |   2020 | Demonstration Papers I                                                              | excluded      | heading:excluded             |  11 |            4   |
| SIGIR   |   2020 | Demonstration Papers II                                                             | excluded      | heading:excluded             |  11 |            4   |
| SIGIR   |   2020 | Keynotes and Invited Talks                                                          | excluded      | heading:excluded             |   8 |            1   |
| SIGIR   |   2020 | Tutorials                                                                           | excluded      | heading:excluded             |   8 |            4   |
| SIGIR   |   2020 | Workshops                                                                           | excluded      | heading:excluded             |   8 |            3.5 |
| SIGIR   |   2020 | Industry (SIRIP) Papers I                                                           | excluded      | heading:industry+pages:short |   1 |            7   |
| SIGIR   |   2020 | Session 2A: Knowledge for Personalization                                           | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2020 | Session 2B: User Behavior and Experience                                            | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2020 | Session 2C: Evaluation                                                              | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2020 | Session 1A: NeuIR and Semantic Matching                                             | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 1B: Knowledge and Explainability                                            | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 1C: Graph-based Analysis                                                    | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 3A: Bias and Fairness                                                       | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 3B: Learning to Rank                                                        | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 3C: Question Answering                                                      | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 4A: Query and Representation                                                | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 4B: Graph-based Recommendation                                              | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 4C: Neural Networks and Embedding                                           | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 5A: Domain Specific Applications 1                                          | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 5B: Learning for Recommendation                                             | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 5C: Information Access and Filtering                                        | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 6A: Neural Collaborative Filtering 1                                        | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 6B: Domain Specific Applications 2                                          | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 6C: Context-aware Modeling                                                  | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 7A: Conversation and Interactive IR                                         | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 7B: Text Classification and Transfer Learning                               | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 7C: Neural Collaborative Filtering 2                                        | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 8A: Domain Specific Retrieval Tasks                                         | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 8B: Multi-modal Retrieval and Ranking                                       | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Session 8C: Sequential Recommendation                                               | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2020 | Industry (SIRIP) Papers II                                                          | industry      | heading:industry             |  11 |           10   |
| SIGIR   |   2020 | Industry (SIRIP) Papers I                                                           | industry      | heading:industry             |  10 |           10   |
| SIGIR   |   2020 | Short Research Papers I                                                             | short         | heading:short                |  77 |            4   |
| SIGIR   |   2020 | Short Research Papers II                                                            | short         | heading:short                |  76 |            4   |
| SIGIR   |   2021 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  11 |            1   |
| SIGIR   |   2021 | SIRIP papers                                                                        | excluded      | heading:industry+pages:short |   9 |            2   |
| SIGIR   |   2021 | Tutorials                                                                           | excluded      | heading:excluded             |   9 |            4   |
| SIGIR   |   2021 | Demonstration Papers I                                                              | excluded      | heading:excluded             |   7 |            5   |
| SIGIR   |   2021 | Demonstration Papers II                                                             | excluded      | heading:excluded             |   7 |            5   |
| SIGIR   |   2021 | Demonstration Papers III                                                            | excluded      | heading:excluded             |   6 |            5   |
| SIGIR   |   2021 | Workshops                                                                           | excluded      | heading:excluded             |   6 |            4   |
| SIGIR   |   2021 | Session 1A: Bias and counterfactual learning 1                                      | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 1E: Knowledge Structures                                                    | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 1F: Applications 1                                                          | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 2C: Sequences and Sessions                                                  | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 2D: Time Matters                                                            | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 2E: Question Answering                                                      | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 3A: Conversational IR 1                                                     | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2021 | Session 3B: Recommendation 3                                                        | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 3C: Neural IR                                                               | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 3D: Cross-domain IR                                                         | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 3E: Diversity and Novelty                                                   | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 4B: Recommendation 4                                                        | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 4C: Learning to Rank                                                        | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 4D: Legal IR                                                                | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 4E: Fairness                                                                | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 5A: Multi-modal IR                                                          | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2021 | Session 5B: Exploration and Cold Start                                              | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 5C: Mining and Classification                                               | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 5D: Click Models and Prediction                                             | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 5E: Efficiency                                                              | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2021 | Session 1B: Recommendation 1                                                        | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 1C: Searching and Ranking                                                   | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 1D: Social Aspects                                                          | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 2A: Bias and Counterfactual Learning 2                                      | full          | pages:full                   |   4 |           10.5 |
| SIGIR   |   2021 | Session 4A: Conversational IR 2                                                     | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 4F: Adversarial IR                                                          | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 6A: Multimedia IR                                                           | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 6B: Reinforcement Learning and Bandits                                      | full          | pages:full                   |   4 |           10.5 |
| SIGIR   |   2021 | Session 6C: Natural Language and Semantics                                          | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 6D: IR Models                                                               | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2021 | Session 2B: Recommendation 2                                                        | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2021 | Session 3F: Applications 3                                                          | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2021 | Session 6E: Evaluation                                                              | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2021 | Session 2F: Applications 2                                                          | full          | pages:full                   |   2 |           10.5 |
| SIGIR   |   2021 | Resource Papers III                                                                 | other_track   | heading:other_track          |  10 |            7   |
| SIGIR   |   2021 | Resource Papers II                                                                  | other_track   | heading:other_track          |   9 |            7   |
| SIGIR   |   2021 | Resource Papers I                                                                   | other_track   | heading:other_track          |   8 |            7   |
| SIGIR   |   2021 | Perspectives Papers                                                                 | other_track   | heading:other_track          |   3 |           11   |
| SIGIR   |   2021 | Short Research Papers III                                                           | short         | heading:short                |  49 |            5   |
| SIGIR   |   2021 | Short Research Papers I                                                             | short         | heading:short                |  48 |            5   |
| SIGIR   |   2021 | Short Research Papers II                                                            | short         | heading:short                |  48 |            5   |
| SIGIR   |   2022 | Demo Papers                                                                         | excluded      | heading:excluded             |  25 |            5   |
| SIGIR   |   2022 | SIRIP Papers                                                                        | excluded      | heading:industry+pages:short |  15 |            5   |
| SIGIR   |   2022 | Tutorials                                                                           | excluded      | heading:excluded             |  12 |            4   |
| SIGIR   |   2022 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  10 |            1   |
| SIGIR   |   2022 | Workshops                                                                           | excluded      | heading:excluded             |   8 |            4   |
| SIGIR   |   2022 | Keynote Talks                                                                       | excluded      | heading:excluded             |   4 |            1   |
| SIGIR   |   2022 | Topic 18: Recommender Systems                                                       | full          | pages:full                   |  19 |           11   |
| SIGIR   |   2022 | Topic 6: Domain-Specific IR                                                         | full          | pages:full                   |  13 |           11   |
| SIGIR   |   2022 | Topic 3: Conversational IR                                                          | full          | pages:full                   |  12 |           11   |
| SIGIR   |   2022 | Topic 11: IR Models                                                                 | full          | pages:full                   |   9 |           11   |
| SIGIR   |   2022 | Topic 19: Search and Ranking                                                        | full          | pages:full                   |   9 |           11   |
| SIGIR   |   2022 | Topic 15: NLP and Semantics                                                         | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2022 | Topic 8: Evaluation and User Studies                                                | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2022 | Topic 10: Fairness in IR                                                            | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2022 | Topic 16: POI and News Recommendations                                              | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2022 | Topic 1: Bias in IR                                                                 | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2022 | Topic 21: Sequential Recommendations                                                | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2022 | Topic 2: Collaborative Filtering                                                    | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2022 | Topic 12: Knowledge Graphs                                                          | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2022 | Topic 13: Multi- and Cross-modal IR                                                 | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2022 | Topic 20: Sentiment Analysis and Classification                                     | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2022 | Topic 22: Session-based and Group Recommendation                                    | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2022 | Topic 23: Social Aspects                                                            | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2022 | Topic 4: Cross Domain IR                                                            | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2022 | Topic 5: CTR and Conversion Rate Prediction                                         | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2022 | Topic 9: Explainable Search and Recommendation                                      | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2022 | Topic 14: Multimedia IR                                                             | full          | pages:full                   |   4 |           10.5 |
| SIGIR   |   2022 | Topic 17: Question Answering                                                        | full          | pages:full                   |   4 |           11   |
| SIGIR   |   2022 | Topic 7: Efficiency                                                                 | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2022 | Resource Track Papers                                                               | other_track   | heading:other_track          |  30 |           11   |
| SIGIR   |   2022 | Perspective Papers                                                                  | other_track   | heading:other_track          |   7 |           12   |
| SIGIR   |   2022 | Reproducibility Track Papers                                                        | other_track   | heading:other_track          |   7 |           11   |
| SIGIR   |   2022 | Short Research Papers                                                               | short         | heading:short                | 165 |            6   |
| SIGIR   |   2023 | SIRIP Papers                                                                        | excluded      | heading:industry+pages:short |  40 |            5   |
| SIGIR   |   2023 | Demo Papers                                                                         | excluded      | heading:excluded             |  26 |            5   |
| SIGIR   |   2023 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  11 |            1   |
| SIGIR   |   2023 | Tutorials                                                                           | excluded      | heading:excluded             |   8 |            4   |
| SIGIR   |   2023 | Workshops                                                                           | excluded      | heading:excluded             |   8 |            4   |
| SIGIR   |   2023 | Keynote Talks                                                                       | excluded      | heading:excluded             |   4 |            1.5 |
| SIGIR   |   2023 | Session 22 - Collaborative Filtering                                                | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2023 | Session 24 - Cross-modal, Cross-lingual, Multi-modal                                | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2023 | Session 25 - E-commerce & Other Applications                                        | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2023 | Session 10 - Sparsity Problem                                                       | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2023 | Session 23 - Cold-start Recommendation and Users' Preferences & Interests           | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2023 | Session 26 - Query Performance and CTR Prediction                                   | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2023 | Session 3 - Dense Retrieval                                                         | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2023 | Session 4 - Language Models                                                         | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2023 | Session 6 - Sequential Recommendation - Part 2                                      | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2023 | Session 9 - Music, video, Social Media                                              | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2023 | Session 1 - Unbiased and Fairness                                                   | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 14 - Efficiency                                                             | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2023 | Session 15 - Crowdsourced and Annotation                                            | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 17 - Temporal & Dynamic - Part 1                                            | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 18 - Knowledge Graphs - Part 2                                              | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2023 | Session 19 - Implicit Feedback and Sessions                                         | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 2 - Sequential Recommendation - Part 1                                      | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 20 - Personalized Models                                                    | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 21 - Legal, Medicine & Health                                               | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 27 - Summarisation & Text Generation                                        | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 29 - Multimodal & Multimedia                                                | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 30 - Temporal & Dynamic - Part 2                                            | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 31 - Implicit Feedback and Sessions                                         | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 8 - POI Recommendation                                                      | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2023 | Session 12 - Knowledge Graphs - Part 1                                              | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2023 | Session 28 - Cross-domain Recommendation                                            | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2023 | Session 33 - Attacks and Other Recommender Systems                                  | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2023 | Session 5 - Exposure and Popularity Bias                                            | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2023 | Session 7 - Knowledge Graphs for Recommendation                                     | full          | pages:full                   |   4 |           10.5 |
| SIGIR   |   2023 | Session 11 - Evaluation                                                             | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2023 | Session 13 - Conversational Search and Recommendation                               | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2023 | Session 16 - Question Answering                                                     | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2023 | Session 32 - Collaborative Filtering & Graph Neural Approaches                      | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2023 | Resource Papers                                                                     | other_track   | heading:other_track          |  40 |           10   |
| SIGIR   |   2023 | Reproducibility Papers                                                              | other_track   | heading:other_track          |   7 |           10   |
| SIGIR   |   2023 | Perspective Papers                                                                  | other_track   | heading:other_track          |   6 |           10.5 |
| SIGIR   |   2023 | Short Research Papers                                                               | short         | heading:short                | 154 |            5   |
| SIGIR   |   2024 | Session: Demo Papers                                                                | excluded      | heading:excluded             |  22 |            5   |
| SIGIR   |   2024 | Session: Workshops                                                                  | excluded      | heading:excluded             |  13 |            4   |
| SIGIR   |   2024 | Session: Tutorials                                                                  | excluded      | heading:excluded             |  10 |            4   |
| SIGIR   |   2024 | Session: Doctoral Consortium                                                        | excluded      | heading:excluded             |   9 |            1   |
| SIGIR   |   2024 | Session: SIRIP: E-commerce                                                          | excluded      | heading:industry+pages:short |   6 |            5   |
| SIGIR   |   2024 | Session: SIRIP: Recsys and Social Media                                             | excluded      | heading:industry+pages:short |   6 |            5   |
| SIGIR   |   2024 | Session: SIRIP: LLMs 1                                                              | excluded      | heading:industry+pages:short |   5 |            5   |
| SIGIR   |   2024 | Session: SIRIP: Domain-Specific 1                                                   | excluded      | heading:industry+pages:short |   4 |            5   |
| SIGIR   |   2024 | Session: SIRIP: Search Assistance                                                   | excluded      | heading:industry+pages:short |   4 |            5   |
| SIGIR   |   2024 | Session: SIRIP: Domain-Specific 2                                                   | excluded      | heading:industry+pages:short |   3 |            5   |
| SIGIR   |   2024 | Session: SIRIP: LLMs 2                                                              | excluded      | heading:industry+pages:short |   3 |            5   |
| SIGIR   |   2024 | Keynote Talks                                                                       | excluded      | heading:excluded             |   1 |            2   |
| SIGIR   |   2024 | Session: SIRIP: Panel                                                               | excluded      | heading:excluded             |   1 |            2   |
| SIGIR   |   2024 | Domain Specific                                                                     | full          | pages:full                   |   9 |           10   |
| SIGIR   |   2024 | Session: Question Answering and Summarisation                                       | full          | pages:full                   |   9 |           11   |
| SIGIR   |   2024 | Session: Reasoning and Knowledge Graphs                                             | full          | pages:full                   |   8 |           10.5 |
| SIGIR   |   2024 | Session: Conversational IR and Recommendation                                       | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2024 | Session: Cross-Domain Recommendation                                                | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2024 | Session: Evaluation                                                                 | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2024 | Session: Networks and Graphs                                                        | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2024 | Session: Privacy, Security and Federated Learning                                   | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2024 | Session: RecSys and LLMs                                                            | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2024 | Session: Recommendation Systems                                                     | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2024 | Session: Sequential Recommendation                                                  | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2024 | CTR, Ads and Click Models                                                           | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2024 | Session: Evaluation with and for LLMs                                               | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2024 | Session: Fairness                                                                   | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2024 | Session: Fairness in RecSys                                                         | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2024 | Session: Graphs and RecSys 2                                                        | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2024 | Session: Legal                                                                      | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2024 | Session: Domain Specific RecSys                                                     | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: Efficiency for Search                                                      | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: LLMs and Search                                                            | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: Long-term and Session Recommendation                                       | full          | heading:full                 |   5 |           11   |
| SIGIR   |   2024 | Session: Multimedia 1                                                               | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: Multimodal                                                                 | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2024 | Session: Multimodal RecSys                                                          | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2024 | Session: NLP                                                                        | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: Neural IR                                                                  | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2024 | Session: Point-of-Interest Recommendation                                           | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: Retrieval Augmented Generation                                             | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2024 | Session: Dense Retrieval 1                                                          | full          | pages:full                   |   4 |           11   |
| SIGIR   |   2024 | Session: Diffusion in RecSys                                                        | full          | pages:full                   |   4 |           10   |
| SIGIR   |   2024 | Session: Multimedia 2                                                               | full          | pages:full                   |   4 |           11   |
| SIGIR   |   2024 | Session: Prompts, Instructions and LLMs in Recommender Systems                      | full          | pages:full                   |   4 |           11   |
| SIGIR   |   2024 | Session: Users and Simulations                                                      | full          | pages:full                   |   4 |           11   |
| SIGIR   |   2024 | Session: Dense Retrieval 2                                                          | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2024 | Session: Explanability in Search and Recommendation                                 | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2024 | Session: GenIR and The Future of Search with LLMs                                   | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2024 | Session: Graphs and LLMs                                                            | full          | pages:full                   |   3 |           10   |
| SIGIR   |   2024 | Session: Multilingual Retrieval                                                     | full          | pages:full                   |   3 |           11   |
| SIGIR   |   2024 | Session: Graphs and RecSys 1                                                        | full          | pages:full                   |   2 |           10.5 |
| SIGIR   |   2024 | Session: Short Research Papers                                                      | short         | heading:short                |  87 |            5   |
| SIGIR   |   2024 | Domain Specific                                                                     | short         | pages:short                  |   2 |            6.5 |
| SIGIR   |   2024 | Session: NLP                                                                        | short         | pages:short                  |   1 |            6   |
| SIGIR   |   2025 | SIRIP                                                                               | excluded      | heading:industry+pages:short |  35 |            5   |
| SIGIR   |   2025 | Demo Papers                                                                         | excluded      | heading:excluded             |  26 |            5   |
| SIGIR   |   2025 | Workshop Summaries                                                                  | excluded      | heading:excluded             |  16 |            4   |
| SIGIR   |   2025 | Tutorials                                                                           | excluded      | heading:excluded             |  14 |            4   |
| SIGIR   |   2025 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  11 |            1   |
| SIGIR   |   2025 | Keynotes                                                                            | excluded      | heading:excluded             |   3 |            2   |
| SIGIR   |   2025 | Domain-specific Applications 1                                                      | full          | pages:full                   |   8 |           10.5 |
| SIGIR   |   2025 | Image Retrieval                                                                     | full          | pages:full                   |   8 |           10   |
| SIGIR   |   2025 | Machine Learning 1                                                                  | full          | pages:full                   |   8 |           10   |
| SIGIR   |   2025 | Multi-modal Retrieval                                                               | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2025 | Natural Language Processing 1                                                       | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2025 | RecSys: Domain-specific                                                             | full          | pages:full                   |   8 |           10   |
| SIGIR   |   2025 | RecSys: Ranking and Adaptivity                                                      | full          | pages:full                   |   8 |           10   |
| SIGIR   |   2025 | RecSys: Sequential 1                                                                | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2025 | RecSys: Sequential 2                                                                | full          | pages:full                   |   8 |           10   |
| SIGIR   |   2025 | Reranking                                                                           | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2025 | Search and Ranking 1                                                                | full          | pages:full                   |   8 |           11   |
| SIGIR   |   2025 | Video Retrieval                                                                     | full          | pages:full                   |   8 |           10.5 |
| SIGIR   |   2025 | Conversational IR and Intelligent Agents                                            | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2025 | Domain-specific Applications 2                                                      | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2025 | Humans and Interfaces                                                               | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2025 | Knowledge and Knowledge Graphs                                                      | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2025 | RecSys: Graphs                                                                      | full          | pages:full                   |   7 |           11   |
| SIGIR   |   2025 | RecSys: Multimodal                                                                  | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2025 | RecSys: Scalability, Embeddings and Training                                        | full          | pages:full                   |   7 |           10   |
| SIGIR   |   2025 | Efficiency                                                                          | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2025 | Evaluation                                                                          | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2025 | FATE 1                                                                              | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2025 | FATE 2                                                                              | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2025 | Natural Language Processing 2                                                       | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2025 | Natural Language Processing 3                                                       | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2025 | RecSys: Collaborative Filtering                                                     | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2025 | RecSys: FATE                                                                        | full          | pages:full                   |   6 |           10   |
| SIGIR   |   2025 | RecSys: LLMs                                                                        | full          | pages:full                   |   6 |           10.5 |
| SIGIR   |   2025 | Search and Ranking 2                                                                | full          | pages:full                   |   6 |           11   |
| SIGIR   |   2025 | Biomedical and Health                                                               | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2025 | FATE 3                                                                              | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2025 | Machine Learning 2                                                                  | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2025 | Question Answering                                                                  | full          | pages:full                   |   5 |           11   |
| SIGIR   |   2025 | RecSys: Sequential 3                                                                | full          | pages:full                   |   5 |           10   |
| SIGIR   |   2025 | Resource Papers                                                                     | other_track   | heading:other_track          |  43 |           11   |
| SIGIR   |   2025 | Reproducibility Papers                                                              | other_track   | heading:other_track          |  27 |           10   |
| SIGIR   |   2025 | Low Resource Environment Papers                                                     | other_track   | heading:other_track          |  10 |            3   |
| SIGIR   |   2025 | Perspective Papers                                                                  | other_track   | heading:other_track          |  10 |           11   |
| SIGIR   |   2025 | Benchmarks and Datasets                                                             | other_track   | heading:other_track          |   6 |           10.5 |
| SIGIR   |   2025 | Short Research Papers                                                               | short         | heading:short                | 106 |            5   |
| WSDM    |   2019 | Demonstration Papers                                                                | excluded      | heading:excluded             |  11 |            4   |
| WSDM    |   2019 | Doctoral Consortium Papers                                                          | excluded      | heading:excluded             |   9 |            2   |
| WSDM    |   2019 | Tutorial Summaries                                                                  | excluded      | heading:excluded             |   7 |            2   |
| WSDM    |   2019 | Keynote & Invited Talks                                                             | excluded      | heading:excluded             |   5 |            1   |
| WSDM    |   2019 | Workshop Summaries                                                                  | excluded      | heading:excluded             |   4 |            2   |
| WSDM    |   2019 | Session 2: Knowledge Graphs and Analytics                                           | full          | pages:full                   |  12 |            9   |
| WSDM    |   2019 | Session 6: Networks and Social Behavior                                             | full          | pages:full                   |  12 |            9   |
| WSDM    |   2019 | Session 9: Recommendation                                                           | full          | pages:full                   |  12 |            9   |
| WSDM    |   2019 | Session 11: Domain Transfer and Representation Learning                             | full          | pages:full                   |   7 |            9   |
| WSDM    |   2019 | Session 4: FATE & Privacy                                                           | full          | pages:full                   |   7 |            9   |
| WSDM    |   2019 | Session 8: Counterfactual and Causal Learning                                       | full          | pages:full                   |   7 |            9   |
| WSDM    |   2019 | Session 10: Personalization and Characterizing User Behavior                        | full          | pages:full                   |   5 |            9   |
| WSDM    |   2019 | Session 3: Recommendation and Temporal Trends                                       | full          | pages:full                   |   5 |            9   |
| WSDM    |   2019 | Session 7: E-commerce and Recommendation                                            | full          | pages:full                   |   5 |            9   |
| WSDM    |   2019 | Session 12: Text Understanding                                                      | full          | pages:full                   |   4 |            9   |
| WSDM    |   2019 | Session 1: Search and Ranking                                                       | full          | pages:full                   |   4 |            9   |
| WSDM    |   2019 | Session 5: Understanding Conversation, Discussion, and Opinions                     | full          | pages:full                   |   4 |            9   |
| WSDM    |   2020 | Demonstrations                                                                      | excluded      | heading:excluded             |  10 |            4   |
| WSDM    |   2020 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |  10 |            2   |
| WSDM    |   2020 | Tutorials                                                                           | excluded      | heading:excluded             |   9 |            4   |
| WSDM    |   2020 | Workshop Summaries                                                                  | excluded      | heading:excluded             |   6 |            2   |
| WSDM    |   2020 | Keynote Talks                                                                       | excluded      | heading:excluded             |   4 |            1.5 |
| WSDM    |   2020 | Technical Presentations                                                             | full          | heading:full                 |  91 |            9   |
| WSDM    |   2021 | Demo Session I                                                                      | excluded      | heading:excluded             |  11 |            4   |
| WSDM    |   2021 | Demo Session II                                                                     | excluded      | heading:excluded             |  11 |            4   |
| WSDM    |   2021 | Tutorials                                                                           | excluded      | heading:excluded             |  10 |            3.5 |
| WSDM    |   2021 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |   7 |            2   |
| WSDM    |   2021 | Workshops                                                                           | excluded      | heading:excluded             |   5 |            2   |
| WSDM    |   2021 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| WSDM    |   2021 | Poster Session I                                                                    | full          | pages:full                   |  27 |            9   |
| WSDM    |   2021 | Poster Session II                                                                   | full          | pages:full                   |  15 |            9   |
| WSDM    |   2021 | Session 12: Ranking                                                                 | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 13: Knowledge                                                               | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 14: Temporal Data and Forecasting                                           | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 2: Classification                                                           | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 3: Recommender Systems                                                      | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 4: Networks                                                                 | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 7: Clustering and Representation Learning                                   | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 8: Web Analysis                                                             | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 9: Search and Recommendation                                                | full          | pages:full                   |   6 |            9   |
| WSDM    |   2021 | Session 10: Explainability and Intervention                                         | full          | pages:full                   |   3 |            9   |
| WSDM    |   2021 | Session 11: Fairness                                                                | full          | pages:full                   |   3 |            9   |
| WSDM    |   2021 | Session 1: Society                                                                  | full          | pages:full                   |   3 |            9   |
| WSDM    |   2021 | Session 5: Experiments                                                              | full          | pages:full                   |   3 |            9   |
| WSDM    |   2021 | Session 6: eCommerce                                                                | full          | pages:full                   |   3 |            9   |
| WSDM    |   2022 | Demonstrations                                                                      | excluded      | heading:excluded             |  14 |            4   |
| WSDM    |   2022 | Industry Day Talks                                                                  | excluded      | heading:excluded             |  14 |            1   |
| WSDM    |   2022 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |   9 |            2   |
| WSDM    |   2022 | Tutorial Presentations                                                              | excluded      | heading:excluded             |   7 |            3   |
| WSDM    |   2022 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            1   |
| WSDM    |   2022 | Smart City Talks                                                                    | excluded      | heading:excluded             |   3 |            1   |
| WSDM    |   2022 | Research Papers                                                                     | full          | pages:full                   | 159 |            9   |
| WSDM    |   2022 | Research Papers                                                                     | short         | pages:short                  |   1 |            7   |
| WSDM    |   2023 | Demo Session I                                                                      | excluded      | heading:excluded             |  12 |            4   |
| WSDM    |   2023 | Demo Session II                                                                     | excluded      | heading:excluded             |  11 |            4   |
| WSDM    |   2023 | Industry Day                                                                        | excluded      | heading:industry+pages:short |  10 |            2   |
| WSDM    |   2023 | Tutorials                                                                           | excluded      | heading:excluded             |  10 |            4   |
| WSDM    |   2023 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |   8 |            2   |
| WSDM    |   2023 | Workshops                                                                           | excluded      | heading:excluded             |   5 |            2   |
| WSDM    |   2023 | Keynote Talks                                                                       | excluded      | heading:excluded             |   3 |            2   |
| WSDM    |   2023 | Poster Session                                                                      | full          | pages:full                   |  71 |            9   |
| WSDM    |   2023 | Session 1: Social Issues in Data Mining                                             | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 2: Recommender Systems I                                                    | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 3: Graph Neural Networks                                                    | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 5: Recommender Systems II                                                   | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 6: Learning                                                                 | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 7: Graph Mining                                                             | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 8: Recommendation and Learning                                              | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 9: Language Models and Text Mining                                          | full          | pages:full                   |   6 |            9   |
| WSDM    |   2023 | Session 4: Best of WSDM 2023                                                        | full          | pages:full                   |   4 |            9   |
| WSDM    |   2023 | Smart City Day                                                                      | short         | pages:short                  |   5 |            2   |
| WSDM    |   2024 | Short Demo Papers                                                                   | excluded      | heading:excluded             |  17 |            4   |
| WSDM    |   2024 | Industry Day Talk Abstracts                                                         | excluded      | heading:excluded             |  16 |            2   |
| WSDM    |   2024 | Doctoral Consortiums                                                                | excluded      | heading:excluded             |   9 |            3   |
| WSDM    |   2024 | Tutorial Papers                                                                     | excluded      | heading:excluded             |   7 |            4   |
| WSDM    |   2024 | WSDM Day Talk Abstracts                                                             | excluded      | heading:excluded             |   6 |            2   |
| WSDM    |   2024 | Workshop Abstracts                                                                  | excluded      | heading:excluded             |   6 |            2   |
| WSDM    |   2024 | Keynote Talk Abstracts                                                              | excluded      | heading:excluded             |   5 |            1   |
| WSDM    |   2024 | Full Research Papers                                                                | full          | heading:full                 | 109 |            9   |
| WSDM    |   2025 | Demonstrations                                                                      | excluded      | heading:excluded             |  11 |            4   |
| WSDM    |   2025 | Industry Day Talks                                                                  | excluded      | heading:excluded             |   9 |            2   |
| WSDM    |   2025 | Tutorials                                                                           | excluded      | heading:excluded             |   9 |            4   |
| WSDM    |   2025 | WSDM Day Talks                                                                      | excluded      | heading:excluded             |   6 |            2   |
| WSDM    |   2025 | Doctoral Consortium                                                                 | excluded      | heading:excluded             |   5 |            3   |
| WSDM    |   2025 | Plenary Session 1: Graph Neural Networks and Inferences                             | excluded      | heading:excluded             |   5 |           10   |
| WSDM    |   2025 | Plenary Session 2: Recommendation Systems                                           | excluded      | heading:excluded             |   5 |           10   |
| WSDM    |   2025 | Plenary Session 3: Large Language Models                                            | excluded      | heading:excluded             |   5 |           10   |
| WSDM    |   2025 | Plenary Session 5: Graph Learning and Adaptation                                    | excluded      | heading:excluded             |   5 |            9   |
| WSDM    |   2025 | Workshops                                                                           | excluded      | heading:excluded             |   5 |            2   |
| WSDM    |   2025 | Plenary Session 4: Sequential and Temporal Data Modeling                            | excluded      | heading:excluded             |   4 |            9   |
| WSDM    |   2025 | Plenary Session 6: Fake News and Anomaly Detection                                  | excluded      | heading:excluded             |   4 |            9   |
| WSDM    |   2025 | Plenary Session 7: Bias in Recommendations                                          | excluded      | heading:excluded             |   4 |            9.5 |
| WSDM    |   2025 | Plenary Session 8: Multimodal Data and Time Series Analysis                         | excluded      | heading:excluded             |   4 |            9   |
| WSDM    |   2025 | Plenary Session 9: Emerging Topics in Data Mining                                   | excluded      | heading:excluded             |   4 |            9.5 |
| WSDM    |   2025 | Poster Session 8                                                                    | full          | pages:full                   |   8 |            9   |
| WSDM    |   2025 | Poster Session 9                                                                    | full          | pages:full                   |   8 |           10   |
| WSDM    |   2025 | Poster Session 1                                                                    | full          | pages:full                   |   7 |           10   |
| WSDM    |   2025 | Poster Session 2                                                                    | full          | pages:full                   |   7 |           10   |
| WSDM    |   2025 | Poster Session 3                                                                    | full          | pages:full                   |   7 |            9   |
| WSDM    |   2025 | Poster Session 4                                                                    | full          | pages:full                   |   7 |            9   |
| WSDM    |   2025 | Poster Session 5                                                                    | full          | pages:full                   |   7 |            9   |
| WSDM    |   2025 | Poster Session 6                                                                    | full          | pages:full                   |   7 |            9   |
| WSDM    |   2025 | Poster Session 7                                                                    | full          | pages:full                   |   7 |           10   |
| WWW     |   2019 | Demos                                                                               | excluded      | heading:excluded             |  28 |            5   |
| WWW     |   2019 | Keynote Talk                                                                        | excluded      | heading:excluded             |   3 |            1   |
| WWW     |   2019 | Full Paper                                                                          | full          | heading:full                 | 225 |           11   |
| WWW     |   2019 | Short Paper                                                                         | short         | heading:short                | 135 |            7   |
| WWW     |   2020 | Keynote Talk                                                                        | excluded      | heading:excluded             |   3 |            1   |
| WWW     |   2020 | Session: Full Paper                                                                 | full          | heading:full                 | 219 |           11   |
| WWW     |   2020 | Session: Short Paper                                                                | short         | heading:short                |  97 |            7   |
| WWW     |   2020 | Session: Future of the Web Track                                                    | short         | pages:short                  |   1 |            3   |
| WWW     |   2021 | Session: Recommendations                                                            | full          | pages:full                   |  29 |           12   |
| WWW     |   2021 | Session: Graph Models                                                               | full          | pages:full                   |  15 |           12   |
| WWW     |   2021 | Session: Mobile and Ubiquitous Computing                                            | full          | pages:full                   |  15 |           12   |
| WWW     |   2021 | Session: Security                                                                   | full          | pages:full                   |  15 |           12   |
| WWW     |   2021 | Session: Bias and Fairness                                                          | full          | pages:full                   |  10 |           12   |
| WWW     |   2021 | Session: Personalization                                                            | full          | pages:full                   |  10 |           11.5 |
| WWW     |   2021 | Session: Question Answering Systems                                                 | full          | pages:full                   |  10 |           11   |
| WWW     |   2021 | Session: Search                                                                     | full          | pages:full                   |  10 |           10.5 |
| WWW     |   2021 | Session: Systems and Infrastructure                                                 | full          | pages:full                   |  10 |           12   |
| WWW     |   2021 | Session: Adversarial Cloaking and Attacks                                           | full          | pages:full                   |   5 |           13   |
| WWW     |   2021 | Session: Applications                                                               | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Auctions and Incentives                                                    | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Crowdsourcing                                                              | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Decomposition and Detection of Anomalies and Motifs                        | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Digital Health                                                             | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Discovery, prediction and recommendation                                   | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Entity Linking and Knowledge Graph Completion                              | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Facts and Misinformation                                                   | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Federated Learning                                                         | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Graph Algorithms                                                           | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Graph Neural Networks                                                      | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Information Extraction                                                     | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Information retrieval                                                      | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Knowledge Extraction                                                       | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Knowledge Graph Embeddings                                                 | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Knowledge Graph Validation                                                 | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Knowledge Graphs                                                           | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Learn to Rank                                                              | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Link prediction                                                            | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Models for networks and dynamics                                           | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Network Algorithms                                                         | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Network Embeddings                                                         | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Networks, Access and Content Quality                                       | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Neural Networks                                                            | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Online Advertising                                                         | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Online Advertising and Pricing                                             | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Online Conversations                                                       | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Online Markets                                                             | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Ontologies and Knowledge Extraction                                        | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Politics on the Web                                                        | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Privacy                                                                    | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Question Answering and Text Processing                                     | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Relevance, Ranking and Recommendations                                     | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Sampling                                                                   | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Sentiment                                                                  | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Special networks and dynamics                                              | full          | pages:full                   |   5 |           11   |
| WWW     |   2021 | Session: Text Classification                                                        | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Text Classification and Clustering                                         | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Topic Modeling                                                             | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Urban Computing                                                            | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: User Experience                                                            | full          | pages:full                   |   5 |           12   |
| WWW     |   2021 | Session: Web Mining Applications                                                    | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Web Mining for Search                                                      | full          | pages:full                   |   5 |           10   |
| WWW     |   2021 | Session: Learning                                                                   | full          | pages:full                   |   4 |           12   |
| WWW     |   2021 | Session: User Modeling                                                              | full          | pages:full                   |   4 |           10.5 |
| WWW     |   2021 | Session: Learning                                                                   | short         | pages:short                  |   1 |            8   |
| WWW     |   2021 | Session: Recommendations                                                            | short         | pages:short                  |   1 |            8   |
| WWW     |   2021 | Session: User Modeling                                                              | short         | pages:short                  |   1 |            7   |
| WWW     |   2022 | Session 1 - Keynote Talks                                                           | excluded      | heading:excluded             |   3 |            1   |
| WWW     |   2022 | Session 6 - Research Track: Social Network Analysis and Graph Algorithms            | full          | heading:full                 |  57 |           11   |
| WWW     |   2022 | Session 9 - Research Track: User Modeling, Personalization and Accessibility        | full          | heading:full                 |  57 |           10   |
| WWW     |   2022 | Session 1 - Research Track: Web Mining and Content Analysis                         | full          | heading:full                 |  52 |           10   |
| WWW     |   2022 | Session 3 - Research Track: Search                                                  | full          | heading:full                 |  31 |           10   |
| WWW     |   2022 | Session 5 - Research Track: Semantics and Knowledge                                 | full          | heading:full                 |  27 |           10   |
| WWW     |   2022 | Session 4 - Research Track: Security, Privacy, and Trust                            | full          | heading:full                 |  25 |           11   |
| WWW     |   2022 | Session 10 - Research Track: Web and Society                                        | full          | heading:full                 |  24 |           10   |
| WWW     |   2022 | Session 15 - Special Track: Web for Good                                            | full          | pages:full                   |  24 |           10.5 |
| WWW     |   2022 | Session 2 - Research Track: Economics, Monetization, and Online Markets             | full          | heading:full                 |  18 |           11   |
| WWW     |   2022 | Session 8 - Research Track: Systems and Infrastructure                              | full          | heading:full                 |  15 |           11   |
| WWW     |   2022 | Session 12 - Research Track: Web of Things, Ubiquitous and Mobile Computing         | full          | heading:full                 |  10 |            9.5 |
| WWW     |   2022 | Session 13 - Special Track: Esports and Online Gaming                               | full          | pages:full                   |   8 |           10.5 |
| WWW     |   2022 | Session 7 - Research Track: Social Web                                              | full          | heading:full                 |   7 |           11   |
| WWW     |   2022 | Session 14 - Special Track: History of the Web                                      | other_track   | heading:other_track          |   5 |            8   |
| WWW     |   2022 | Session 15 - Special Track: Web for Good                                            | short         | pages:short                  |   4 |            5   |
| WWW     |   2023 | Keynotes                                                                            | excluded      | heading:excluded             |   5 |            1   |
| WWW     |   2023 | Social Network Analysis and Graph Algorithms                                        | full          | pages:full                   |  71 |           11   |
| WWW     |   2023 | User Modeling and Personalization                                                   | full          | pages:full                   |  61 |           11   |
| WWW     |   2023 | Web Mining and Content Analysis                                                     | full          | pages:full                   |  53 |           10   |
| WWW     |   2023 | Security, Privacy & Trust                                                           | full          | pages:full                   |  38 |           11   |
| WWW     |   2023 | Systems and Infrastructure for Web, Mobile Web, and Web of Things                   | full          | pages:full                   |  28 |           11   |
| WWW     |   2023 | Semantics and Knowledge                                                             | full          | pages:full                   |  25 |           10   |
| WWW     |   2023 | Search                                                                              | full          | pages:full                   |  24 |           11   |
| WWW     |   2023 | Web4Good                                                                            | full          | pages:full                   |  23 |           10   |
| WWW     |   2023 | Web & Society                                                                       | full          | pages:full                   |  20 |           11   |
| WWW     |   2023 | Economics, Monetization, and Online Markets                                         | full          | pages:full                   |  19 |           11   |
| WWW     |   2023 | Fairness, Accountability, Transparency and Ethics on the Web                        | full          | pages:full                   |  16 |           11   |
| WWW     |   2023 | Crowdsourcing and Human Computation                                                 | full          | pages:full                   |   7 |           10   |
| WWW     |   2023 | The Creative Web                                                                    | full          | pages:full                   |   4 |           10.5 |
| WWW     |   2023 | Web4Good                                                                            | short         | pages:short                  |   8 |            5.5 |
| WWW     |   2023 | The Creative Web                                                                    | short         | pages:short                  |   3 |            5   |
| WWW     |   2023 | Economics, Monetization, and Online Markets                                         | short         | pages:short                  |   1 |            8   |
| WWW     |   2023 | Web Mining and Content Analysis                                                     | short         | pages:short                  |   1 |            8   |
| WWW     |   2024 | Keynotes                                                                            | excluded      | heading:excluded             |   4 |            1   |
| WWW     |   2024 | Research Track: User Modeling and Recommendation                                    | full          | heading:full                 |  76 |           11.5 |
| WWW     |   2024 | Research Track: Graph Algorithms and Learning for the Web                           | full          | heading:full                 |  69 |           12   |
| WWW     |   2024 | Research Track: Web Mining and Content Analysis                                     | full          | heading:full                 |  48 |           11   |
| WWW     |   2024 | Research Track: Systems and Infrastructure for Web, Mobile, and WoT                 | full          | heading:full                 |  39 |           11   |
| WWW     |   2024 | Research Track: Semantics and Knowledge                                             | full          | heading:full                 |  36 |           11   |
| WWW     |   2024 | Research Track: Security                                                            | full          | heading:full                 |  35 |           12   |
| WWW     |   2024 | Research Track: Social Networks, Social Media, and Society                          | full          | heading:full                 |  33 |           12   |
| WWW     |   2024 | Research Track: Economics, Online Markets, and Human Computation                    | full          | heading:full                 |  27 |           11   |
| WWW     |   2024 | Special Track: Web4Good                                                             | full          | pages:full                   |  23 |           11   |
| WWW     |   2024 | Research Track: Responsible Web                                                     | full          | heading:full                 |  22 |           11.5 |
| WWW     |   2024 | Research Track: Search                                                              | full          | heading:full                 |  20 |           11   |
| WWW     |   2025 | Keynote Talks                                                                       | excluded      | heading:excluded             |   5 |            1   |
| WWW     |   2025 | Web4Good Track Papers                                                               | full          | pages:full                   |  33 |           11   |
| WWW     |   2025 | Poster Session 3                                                                    | full          | pages:full                   |  31 |           12   |
| WWW     |   2025 | Poster Session 5                                                                    | full          | pages:full                   |  31 |           12   |
| WWW     |   2025 | Poster Session 8                                                                    | full          | pages:full                   |  31 |           12   |
| WWW     |   2025 | Poster Session 7                                                                    | full          | pages:full                   |  28 |           11.5 |
| WWW     |   2025 | Poster Session 1                                                                    | full          | pages:full                   |  27 |           12   |
| WWW     |   2025 | Poster Session 4                                                                    | full          | pages:full                   |  27 |           12   |
| WWW     |   2025 | Poster Session 6                                                                    | full          | pages:full                   |  27 |           11   |
| WWW     |   2025 | Poster Session 9                                                                    | full          | pages:full                   |  27 |           12   |
| WWW     |   2025 | Poster Session 2                                                                    | full          | pages:full                   |  25 |           12   |
| WWW     |   2025 | Session 11: Multimodal and Thematic Content Analysis                                | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 12: Blockchain and Web Interoperability                                     | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 13: Web Acceleration and Optimization                                       | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 14: AI for Web Systems                                                      | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 16: Federated Learning and Privacy                                          | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 17: Phishing, Deception, and Consumer Risks                                 | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 18: Blockchain and System Security                                          | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 19: Website Fingerprinting, Browser Security, and Web Authentication        | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 1: Knowledge Representation and Query                                       | full          | pages:full                   |   5 |           13   |
| WWW     |   2025 | Session 20: Graph Foundation Models                                                 | full          | pages:full                   |   5 |           13   |
| WWW     |   2025 | Session 21: Trustworthy Graph Learning                                              | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 22: Complex Graph Learning                                                  | full          | pages:full                   |   5 |           13   |
| WWW     |   2025 | Session 23: Classical Graph Learning                                                | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 24: Auctions and Games                                                      | full          | pages:full                   |   5 |            9   |
| WWW     |   2025 | Session 25: Data, Incentives and Applications                                       | full          | pages:full                   |   5 |           15   |
| WWW     |   2025 | Session 27: Responsible Web: Methods and Applications                               | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 2: Knowledge and Learning                                                   | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 31: Generative AI for the Web                                               | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 32: People, Platforms, and Personalization                                  | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 3: Data and Semantics                                                       | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 4: Large Language Models in Recommendation                                  | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 5: Visual and Multimodal Systems                                            | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 6: Graph and Social Network Based Approaches                                | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 7: Reinforcement Learning and Sequential Methods                            | full          | pages:full                   |   5 |           11   |
| WWW     |   2025 | Session 8: Optimization and Learning Methods                                        | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 9: Graph-Based Social Network Analysis & Community Detection                | full          | pages:full                   |   5 |           12   |
| WWW     |   2025 | Session 10: Online Behavior, Sentiment, and Influence                               | full          | pages:full                   |   4 |           13.5 |
| WWW     |   2025 | Session 15: Machine Learning Security and Adversarial Attacks                       | full          | pages:full                   |   4 |           11.5 |
| WWW     |   2025 | Session 28: Retrieval Methods                                                       | full          | pages:full                   |   4 |           12.5 |
| WWW     |   2025 | Session 29: Post Retrieval and Search-based Text Generation                         | full          | pages:full                   |   4 |           13.5 |
| WWW     |   2025 | Session 30: Scalable and Secure Data Processing                                     | full          | pages:full                   |   4 |           12   |
| WWW     |   2025 | Session 26: Ecosystems                                                              | full          | pages:full                   |   3 |           14   |
