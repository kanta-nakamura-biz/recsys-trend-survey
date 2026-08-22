# 推薦関連フィルタの標本監査

汎用会議（SIGIR/KDD/WWW/WSDM/CIKM）のフル論文に対し、
`config/recsys_filter.yaml` の語彙がどう効いているかを無作為標本で確認する。
DBLP はアブストラクトを持たないためタイトルのみでの判定であり、
本文で推薦を扱っていてもタイトルに現れない論文は取りこぼす。

## 抽出された論文（無作為 40 件）

| venue   |   year | title                                                                                                                                |
|:--------|-------:|:-------------------------------------------------------------------------------------------------------------------------------------|
| SIGIR   |   2023 | Blurring-Sharpening Process Models for Collaborative Filtering                                                                       |
| CIKM    |   2022 | Cross-Network Social User Embedding with Hybrid Differential Privacy Guarantees                                                      |
| WWW     |   2024 | Knowledge-Augmented Large Language Models for Personalized Contextual Query Suggestion                                               |
| WSDM    |   2021 | Sparse-Interest Network for Sequential Recommendation                                                                                |
| CIKM    |   2021 | Top-N Recommendation with Counterfactual User Preference Simulation                                                                  |
| WWW     |   2020 | Personalized Employee Training Course Recommendation with Career Development Awareness                                               |
| WWW     |   2020 | Off-policy Learning in Two-stage Recommender Systems                                                                                 |
| WWW     |   2019 | Feature Generation by Convolutional Neural Network for Click-Through Rate Prediction                                                 |
| CIKM    |   2025 | What Data is Really Necessary? A Feasibility Study of Inference Data Minimization for Recommender Systems                            |
| WWW     |   2022 | Large-scale Personalized Video Game Recommendation via Social-aware Contextualized Graph Neural Network                              |
| SIGIR   |   2023 | Generative-Contrastive Graph Learning for Recommendation                                                                             |
| KDD     |   2021 | Table2Charts: Recommending Charts by Learning Shared Table Representations                                                           |
| KDD     |   2023 | A Sublinear Time Algorithm for Opinion Optimization in Directed Social Networks via Edge Recommendation                              |
| WSDM    |   2019 | Top-K Off-Policy Correction for a REINFORCE Recommender System                                                                       |
| KDD     |   2025 | Understanding the Effect of Loss Functions on the Generalization of Recommendations                                                  |
| KDD     |   2022 | Towards Universal Sequence Representation Learning for Recommender Systems                                                           |
| CIKM    |   2019 | Multi-Interest Network with Dynamic Routing for Recommendation at Tmall                                                              |
| CIKM    |   2024 | Behavior-Dependent Linear Recurrent Units for Efficient Sequential Recommendation                                                    |
| KDD     |   2024 | DisCo: Towards Harmonious Disentanglement and Collaboration between Tabular and Semantic Space for Recommendation                    |
| KDD     |   2020 | Kernel Assisted Learning for Personalized Dose Finding                                                                               |
| WWW     |   2022 | Learning Robust Recommenders through Cross-Model Agreement                                                                           |
| CIKM    |   2022 | Personalized Query Suggestion with Searching Dynamic Flow for Online Recruitment                                                     |
| CIKM    |   2025 | Compensating Information and Capturing Modal Preferences in Multimodal Recommendation: A Dual-Path Representation Learning Framework |
| SIGIR   |   2021 | Learning Recommender Systems with Implicit Feedback via Soft Target Enhancement                                                      |
| WSDM    |   2024 | Neural Kalman Filtering for Robust Temporal Recommendation                                                                           |
| CIKM    |   2025 | Benefit from Rich: Tackling Search Interaction Sparsity in Search Enhanced Recommendation                                            |
| SIGIR   |   2024 | An Empirical Analysis on Multi-turn Conversational Recommender Systems                                                               |
| CIKM    |   2022 | Graph Based Long-Term And Short-Term Interest Model for Click-Through Rate Prediction                                                |
| WWW     |   2021 | Leveraging User Behavior History for Personalized Email Search                                                                       |
| SIGIR   |   2024 | ReFer: Retrieval-Enhanced Vertical Federated Recommendation for Full Set User Benefit                                                |
| SIGIR   |   2025 | VoRec: Enhancing Recommendation with Voronoi Diagram in Hyperbolic Space                                                             |
| WSDM    |   2020 | Time Interval Aware Self-Attention for Sequential Recommendation                                                                     |
| SIGIR   |   2024 | Exploring the Individuality and Collectivity of Intents behind Interactions for Graph Collaborative Filtering                        |
| SIGIR   |   2021 | Unsupervised Proxy Selection for Session-based Recommender Systems                                                                   |
| SIGIR   |   2021 | Fairness among New Items in Cold Start Recommender Systems                                                                           |
| WWW     |   2022 | Graph-based Extractive Explainer for Recommendations                                                                                 |
| KDD     |   2024 | Self-Supervised Denoising through Independent Cascade Graph Augmentation for Robust Social Recommendation                            |
| CIKM    |   2021 | Hyperbolic Hypergraphs for Sequential Recommendation                                                                                 |
| KDD     |   2024 | Disentangled Multi-interest Representation Learning for Sequential Recommendation                                                    |
| WWW     |   2024 | Linear-Time Graph Neural Networks for Scalable Recommendations                                                                       |

## 抽出されなかった論文（無作為 40 件・取りこぼし確認用）

| venue   |   year | title                                                                                                                    |
|:--------|-------:|:-------------------------------------------------------------------------------------------------------------------------|
| WWW     |   2022 | Cross DQN: Cross Deep Q Network for Ads Allocation in Feed                                                               |
| WWW     |   2020 | Finding a Choice in a Haystack: Automatic Extraction of Opt-Out Statements from Privacy Policy Text                      |
| WWW     |   2019 | Learning Resolution Parameters for Graph Clustering                                                                      |
| SIGIR   |   2021 | Event Occurrence Date Estimation based on Multivariate Time Series Analysis over Temporal Document Collections           |
| WSDM    |   2024 | TemporalMed: Advancing Medical Dialogues with Time-Aware Responses in Large Language Models                              |
| CIKM    |   2025 | Unsupervised Adversarial Contrastive Hashing for Cross-Modal Retrieval                                                   |
| WSDM    |   2023 | Separating Examination and Trust Bias from Click Predictions for Unbiased Relevance Ranking                              |
| WWW     |   2022 | Exploring Edge Disentanglement for Node Classification                                                                   |
| KDD     |   2020 | Attackability Characterization of Adversarial Evasion Attack on Discrete Data                                            |
| KDD     |   2025 | Connecting Domains and Contrasting Samples: A Ladder for Domain Generalization                                           |
| WWW     |   2021 | Knowledge-Preserving Incremental Social Event Detection via Heterogeneous GNNs                                           |
| KDD     |   2023 | Frigate: Frugal Spatio-temporal Forecasting on Road Networks                                                             |
| KDD     |   2020 | AM-GCN: Adaptive Multi-channel Graph Convolutional Networks                                                              |
| WWW     |   2023 | Efficient Approximation Algorithms for the Diameter-Bounded Max-Coverage Group Steiner Tree Problem                      |
| KDD     |   2024 | Bridging and Compressing Feature and Semantic Spaces for Robust Graph Neural Networks: An Information Theory Perspective |
| CIKM    |   2023 | FARA: Future-aware Ranking Algorithm for Fairness Optimization                                                           |
| CIKM    |   2022 | Explainable Link Prediction in Knowledge Hypergraphs                                                                     |
| CIKM    |   2025 | OASIS: Open-world Adaptive Self-supervised and Imbalanced-aware System                                                   |
| WWW     |   2024 | Spectral Heterogeneous Graph Convolutions via Positive Noncommutative Polynomials                                        |
| CIKM    |   2024 | Veracity Estimation for Entity-Oriented Search with Knowledge Graphs                                                     |
| KDD     |   2020 | The Spectral Zoo of Networks: Embedding and Visualizing Networks with Spectral Moments                                   |
| WWW     |   2022 | This Must Be the Place: Predicting Engagement of Online Communities in a Large-scale Distributed Campaign                |
| KDD     |   2025 | MobileSteward: Integrating Multiple App-Oriented Agents with Self-Evolution to Automate Cross-App Instructions           |
| KDD     |   2025 | Semantics-Aware Patch Encoding and Hierarchical Dependency Modeling for Long-Term Time Series Forecasting                |
| KDD     |   2021 | Towards Robust Prediction on Tail Labels                                                                                 |
| KDD     |   2019 | Separated Trust Regions Policy Optimization Method                                                                       |
| WWW     |   2022 | Allocating Stimulus Checks in Times of Crisis                                                                            |
| WSDM    |   2021 | Optimizing Multiple Performance Metrics with Deep GSP Auctions for E-commerce Advertising                                |
| SIGIR   |   2024 | Ranked List Truncation for Large Language Model-based Re-Ranking                                                         |
| SIGIR   |   2023 | Normalizing Flow-based Neural Process for Few-Shot Knowledge Graph Completion                                            |
| WWW     |   2024 | Predicting and Presenting Task Difficulty for Crowdsourcing Food Rescue Platforms                                        |
| KDD     |   2022 | GPPT: Graph Pre-training and Prompt Tuning to Generalize Graph Neural Networks                                           |
| WWW     |   2021 | Multi-view Graph Contrastive Representation Learning for Drug-Drug Interaction Prediction                                |
| WWW     |   2023 | Impartial Selection with Prior Information                                                                               |
| SIGIR   |   2020 | Fashion Compatibility Modeling through a Multi-modal Try-on-guided Scheme                                                |
| CIKM    |   2025 | Calibrated and Diverse News Coverage                                                                                     |
| SIGIR   |   2024 | GraphGPT: Graph Instruction Tuning for Large Language Models                                                             |
| CIKM    |   2019 | Rating Mechanisms for Sustainability of Crowdsourcing Platforms                                                          |
| SIGIR   |   2023 | Subgraph Search over Neural-Symbolic Graphs                                                                              |
| SIGIR   |   2019 | Interpretable Fashion Matching with Rich Attributes                                                                      |
