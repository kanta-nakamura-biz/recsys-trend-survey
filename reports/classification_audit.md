# トピック分類の標本監査

各軸に分類された論文から無作為抽出したもの。
キーワード辞書（`config/topics.yaml`）と LLM ラベル（`labels/llm_labels.jsonl`）の
判定が妥当かを目視で確認するための資料。`source` は判定の由来を示す。

## 軸ごとの件数と判定の由来

| topic                   | label                      |   keyword |   llm |
|:------------------------|:---------------------------|----------:|------:|
| causal_debiasing        | Causal / Debiasing         |       138 |    34 |
| coldstart_federated     | Cold-start / Federated     |       232 |    67 |
| fairness_explainability | Fairness / Explainability  |       146 |    41 |
| graph                   | Graph / GNN                |       249 |   142 |
| llm                     | LLM-based                  |       167 |    14 |
| multimodal              | Multimodal                 |       118 |     8 |
| reinforcement_learning  | Reinforcement Learning     |       125 |    38 |
| sequential              | Sequential / Session-based |       324 |   109 |

## Graph / GNN（全 391 件から無作為 20 件）

| venue   |   year | title                                                                                                            | source   |
|:--------|-------:|:-----------------------------------------------------------------------------------------------------------------|:---------|
| WSDM    |   2025 | LightGNN: Simple Graph Neural Network for Recommendation                                                         | keyword  |
| CIKM    |   2019 | Fi-GNN: Modeling Feature Interactions via Graph Neural Networks for CTR Prediction                               | keyword  |
| RecSys  |   2023 | KGTORe: Tailored Recommendations through Knowledge-aware GNN Models                                              | keyword  |
| CIKM    |   2022 | The Interaction Graph Auto-encoder Network Based on Topology-aware for Transferable Recommendation               | llm      |
| WWW     |   2024 | Graph Contrastive Learning with Kernel Dependence Maximization for Social Recommendation                         | keyword  |
| SIGIR   |   2024 | Hypergraph Convolutional Network for User-Oriented Fairness in Recommender Systems                               | keyword  |
| WWW     |   2023 | Multi-Behavior Recommendation with Cascading Graph Convolution Networks                                          | keyword  |
| KDD     |   2021 | Multi-view Denoising Graph Auto-Encoders on Heterogeneous Information Networks for Cold-start Recommendation     | keyword  |
| RecSys  |   2022 | TinyKG: Memory-Efficient Training Framework for Knowledge Graph Neural Recommender Systems                       | keyword  |
| SIGIR   |   2023 | Dynamic Graph Evolution Learning for Recommendation                                                              | llm      |
| KDD     |   2021 | MixGCF: An Improved Training Method for Graph Neural Network-based Recommender Systems                           | keyword  |
| SIGIR   |   2019 | Reinforcement Knowledge Graph Reasoning for Explainable Recommendation                                           | keyword  |
| CIKM    |   2022 | Dynamic Hypergraph Learning for Collaborative Filtering                                                          | keyword  |
| WWW     |   2023 | Semi-decentralized Federated Ego Graph Learning for Recommendation                                               | keyword  |
| SIGIR   |   2022 | Post Processing Recommender Systems with Knowledge Graphs for Recency, Popularity, and Diversity of Explanations | keyword  |
| SIGIR   |   2023 | Time-interval Aware Share Recommendation via Bi-directional Continuous Time Dynamic Graphs                       | llm      |
| WWW     |   2023 | MoleRec: Combinatorial Drug Recommendation with Substructure-Aware Molecular Representation Learning             | llm      |
| SIGIR   |   2022 | KETCH: Knowledge Graph Enhanced Thread Recommendation in Healthcare Forums                                       | keyword  |
| KDD     |   2020 | Dual Channel Hypergraph Collaborative Filtering                                                                  | keyword  |
| WWW     |   2021 | RetaGNN: Relational Temporal Attentive Graph Neural Networks for Holistic Sequential Recommendation              | keyword  |

## Sequential / Session-based（全 433 件から無作為 20 件）

| venue   |   year | title                                                                                                     | source   |
|:--------|-------:|:----------------------------------------------------------------------------------------------------------|:---------|
| CIKM    |   2022 | ContrastVAE: Contrastive Variational AutoEncoder for Sequential Recommendation                            | keyword  |
| WWW     |   2023 | Debiased Contrastive Learning for Sequential Recommendation                                               | keyword  |
| WWW     |   2024 | Efficient Noise-Decoupling for Multi-Behavior Sequential Recommendation                                   | keyword  |
| SIGIR   |   2020 | Parameter-Efficient Transfer from Sequential Behaviors for User Modeling and Recommendation               | llm      |
| SIGIR   |   2023 | Dynamic Graph Evolution Learning for Recommendation                                                       | llm      |
| RecSys  |   2019 | Online learning to rank for sequential music recommendation                                               | llm      |
| WSDM    |   2020 | Sequential Recommendation with Dual Side Neighbor-based Collaborative Relation Modeling                   | keyword  |
| CIKM    |   2020 | Star Graph Neural Networks for Session-based Recommendation                                               | keyword  |
| CIKM    |   2025 | Enhancing Multi-Behavior Sequential Recommenders with Behavior-Aware Regularization                       | keyword  |
| SIGIR   |   2025 | AlphaFuse: Learn ID Embeddings for Sequential Recommendation in Null Space of Language Embeddings         | keyword  |
| KDD     |   2025 | Generative Next POI Recommendation with Semantic ID                                                       | keyword  |
| WWW     |   2023 | Dual-interest Factorization-heads Attention for Sequential Recommendation                                 | keyword  |
| WSDM    |   2022 | Heterogeneous Global Graph Neural Networks for Personalized Session-based Recommendation                  | keyword  |
| RecSys  |   2025 | Test-Time Alignment with State Space Model for Tracking User Interest Shifts in Sequential Recommendation | keyword  |
| WSDM    |   2024 | Debiasing Sequential Recommenders through Distributionally Robust Optimization over System Exposure       | keyword  |
| SIGIR   |   2019 | CTRec: A Long-Short Demands Evolution Model for Continuous-Time Recommendation                            | llm      |
| CIKM    |   2022 | Target Interest Distillation for Multi-Interest Recommendation                                            | llm      |
| RecSys  |   2025 | MDSBR: Multimodal Denoising for Session-based Recommendation                                              | keyword  |
| SIGIR   |   2024 | A Generic Behavior-Aware Data Augmentation Framework for Sequential Recommendation                        | keyword  |
| CIKM    |   2022 | Explanation Guided Contrastive Learning for Sequential Recommendation                                     | keyword  |

## Causal / Debiasing（全 172 件から無作為 20 件）

| venue   |   year | title                                                                                                                      | source   |
|:--------|-------:|:---------------------------------------------------------------------------------------------------------------------------|:---------|
| WSDM    |   2020 | Unbiased Recommender Learning from Missing-Not-At-Random Implicit Feedback                                                 | keyword  |
| SIGIR   |   2025 | Exploring the Escalation of Source Bias in User, Data, and Recommender System Feedback Loop                                | llm      |
| SIGIR   |   2021 | Towards Personalized Fairness based on Causal Notion                                                                       | keyword  |
| WSDM    |   2023 | A Causal View for Item-level Effect of Recommendation on User Preference                                                   | keyword  |
| WWW     |   2022 | Rating Distribution Calibration for Selection Bias Mitigation in Recommendations                                           | keyword  |
| WSDM    |   2024 | Debiasing Sequential Recommenders through Distributionally Robust Optimization over System Exposure                        | keyword  |
| WWW     |   2024 | M-scan: A Multi-Scenario Causal-driven Adaptive Network for Recommendation                                                 | keyword  |
| CIKM    |   2025 | Mitigating Latent Confounding Bias in Recommender Systems                                                                  | keyword  |
| CIKM    |   2021 | Counterfactual Review-based Recommendation                                                                                 | keyword  |
| RecSys  |   2020 | Keeping Dataset Biases out of the Simulation: A Debiased Simulator for Reinforcement Learning based Recommender Systems    | keyword  |
| KDD     |   2021 | Popularity Bias in Dynamic Recommendation                                                                                  | keyword  |
| WWW     |   2022 | Cross Pairwise Ranking for Unbiased Item Recommendation                                                                    | keyword  |
| RecSys  |   2020 | Unbiased Ad Click Prediction for Position-aware Advertising Systems                                                        | keyword  |
| RecSys  |   2025 | An Off-Policy Learning Approach for Steering Sentence Generation towards Personalization                                   | keyword  |
| SIGIR   |   2021 | AutoDebias: Learning to Debias for Recommendation                                                                          | keyword  |
| WSDM    |   2022 | Hierarchical Imitation Learning via Subgoal Representation Learning for Dynamic Treatment Recommendation                   | llm      |
| CIKM    |   2023 | Contrastive Counterfactual Learning for Causality-aware Interpretable Recommender Systems                                  | keyword  |
| RecSys  |   2024 | The Role of Unknown Interactions in Implicit Matrix Factorization - A Probabilistic View                                   | llm      |
| RecSys  |   2023 | When Fairness meets Bias: a Debiased Framework for Fairness aware Top-N Recommendation                                     | keyword  |
| CIKM    |   2024 | PACIFIC: Enhancing Sequential Recommendation via Preference-aware Causal Intervention and Counterfactual Data Augmentation | keyword  |

## Fairness / Explainability（全 187 件から無作為 20 件）

| venue   |   year | title                                                                                                                                           | source   |
|:--------|-------:|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| WWW     |   2024 | Retention Depolarization in Recommender System                                                                                                  | keyword  |
| SIGIR   |   2019 | Personalized Fashion Recommendation with Visual Explanations based on Multimodal Attention Network: Towards Visually Explainable Recommendation | keyword  |
| WSDM    |   2020 | Addressing Marketing Bias in Product Recommendations                                                                                            | llm      |
| RecSys  |   2025 | Auditing Recommender Systems for User Empowerment in Very Large Online Platforms under the Digital Services Act                                 | llm      |
| CIKM    |   2025 | Evaluating and Addressing Fairness Across User Groups in Negative Sampling for Recommender Systems                                              | keyword  |
| WWW     |   2024 | Filter Bubble or Homogenization? Disentangling the Long-Term Effects of Recommendations on User Consumption Patterns                            | keyword  |
| SIGIR   |   2024 | Sequential Recommendation with Collaborative Explanation via Mutual Information Maximization                                                    | keyword  |
| RecSys  |   2020 | Ensuring Fairness in Group Recommendations by Rank-Sensitive Balancing of Relevance                                                             | keyword  |
| SIGIR   |   2023 | Rectifying Unfairness in Recommendation Feedback Loop                                                                                           | keyword  |
| RecSys  |   2024 | The Fault in Our Recommendations: On the Perils of Optimizing the Measurable                                                                    | llm      |
| RecSys  |   2025 | You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control                                                  | llm      |
| CIKM    |   2020 | Explainable Recommender Systems via Resolving Learning Representations                                                                          | keyword  |
| CIKM    |   2025 | LeadFairRec: LLM-enhanced Discriminative Counterfactual Debiasing for Two-sided Fairness in Recommendation                                      | keyword  |
| WWW     |   2024 | Uncovering the Deep Filter Bubble: Narrow Exposure in Short-Video Recommendation                                                                | keyword  |
| SIGIR   |   2025 | Enhancing New-item Fairness in Dynamic Recommender Systems                                                                                      | keyword  |
| SIGIR   |   2023 | Measuring Item Global Residual Value for Fair Recommendation                                                                                    | keyword  |
| WWW     |   2021 | ELIXIR: Learning from User Feedback on Explanations to Improve Recommender Models                                                               | keyword  |
| WWW     |   2023 | Maximizing Submodular Functions for Recommendation in the Presence of Biases                                                                    | llm      |
| WWW     |   2020 | Directional and Explainable Serendipity Recommendation                                                                                          | keyword  |
| SIGIR   |   2024 | Configurable Fairness for New Item Recommendation Considering Entry Time of Items                                                               | keyword  |

## Multimodal（全 126 件から無作為 20 件）

| venue   |   year | title                                                                                                            | source   |
|:--------|-------:|:-----------------------------------------------------------------------------------------------------------------|:---------|
| WWW     |   2020 | OutfitNet: Fashion Outfit Recommendation with Attention-Based Multiple Instance Learning                         | llm      |
| RecSys  |   2024 | Not All Videos Become Outdated: Short-Video Recommendation by Learning to Deconfound Release Interval Bias       | keyword  |
| KDD     |   2025 | Preference-Optimized Retrieval and Ranking for Efficient Multimodal Recommendation                               | keyword  |
| CIKM    |   2025 | Learning Invariant Reliability under Diverse Contexts for Robust Multimedia Recommendation                       | keyword  |
| SIGIR   |   2020 | Web-to-Voice Transfer for Product Recommendation on Voice                                                        | llm      |
| RecSys  |   2023 | Understanding and Modeling Passive-Negative Feedback for Short-video Sequential Recommendation                   | keyword  |
| WWW     |   2024 | PromptMM: Multi-Modal Knowledge Distillation for Recommendation with Prompt-Tuning                               | keyword  |
| WSDM    |   2022 | A GNN-based Multi-task Learning Framework for Personalized Video Search                                          | keyword  |
| CIKM    |   2022 | AutoMARS: Searching to Compress Multi-Modality Recommendation Systems                                            | keyword  |
| RecSys  |   2024 | A Multi-modal Modeling Framework for Cold-start Short-video Recommendation                                       | keyword  |
| KDD     |   2019 | A Visual Dialog Augmented Interactive Recommender System                                                         | keyword  |
| CIKM    |   2020 | Multi-modal Knowledge Graphs for Recommender Systems                                                             | keyword  |
| SIGIR   |   2023 | Mining Stable Preferences: Adaptive Modality Decorrelation for Multimedia Recommendation                         | keyword  |
| SIGIR   |   2024 | IISAN: Efficiently Adapting Multimodal Representation for Sequential Recommendation with Decoupled PEFT          | keyword  |
| KDD     |   2024 | LARP: Language Audio Relational Pre-training for Cold-Start Playlist Continuation                                | keyword  |
| KDD     |   2025 | One-shot Multi-view Visual Conversational Recommendation                                                         | keyword  |
| RecSys  |   2023 | Reproducibility Analysis of Recommender Systems relying on Visual Features: traps, pitfalls, and countermeasures | keyword  |
| CIKM    |   2024 | Natural Language-Assisted Multi-modal Medication Recommendation                                                  | keyword  |
| SIGIR   |   2024 | Diffusion Models for Generative Outfit Recommendation                                                            | llm      |
| SIGIR   |   2024 | Multimodality Invariant Learning for Multimedia-Based New Item Recommendation                                    | keyword  |

## Reinforcement Learning（全 163 件から無作為 20 件）

| venue   |   year | title                                                                                                          | source   |
|:--------|-------:|:---------------------------------------------------------------------------------------------------------------|:---------|
| SIGIR   |   2024 | Broadening the View: Demonstration-augmented Prompt Learning for Conversational Recommendation                 | keyword  |
| SIGIR   |   2024 | An Empirical Analysis on Multi-turn Conversational Recommender Systems                                         | keyword  |
| WWW     |   2021 | Intelligent Electric Vehicle Charging Recommendation Based on Multi-Agent Reinforcement Learning               | keyword  |
| WWW     |   2023 | Exploration and Regularization of the Latent Action Space in Recommendation                                    | llm      |
| RecSys  |   2024 | Unleashing the Retrieval Potential of Large Language Models in Conversational Recommender Systems              | keyword  |
| RecSys  |   2023 | Generative Learning Plan Recommendation for Employees: A Performance-aware Reinforcement Learning Approach     | keyword  |
| RecSys  |   2025 | USB-Rec: An Effective Framework for Improving Conversational Recommendation Capability of Large Language Model | keyword  |
| CIKM    |   2021 | Generative Inverse Deep Reinforcement Learning for Online Recommendation                                       | keyword  |
| RecSys  |   2020 | Cascading Hybrid Bandits: Online Learning to Rank for Relevance and Diversity                                  | keyword  |
| SIGIR   |   2020 | MaHRL: Multi-goals Abstraction Based Deep Hierarchical Reinforcement Learning for Recommendations              | keyword  |
| CIKM    |   2025 | STEP: Stepwise Curriculum Learning for Context-Knowledge Fusion in Conversational Recommendation               | keyword  |
| RecSys  |   2021 | Burst-induced Multi-Armed Bandit for Learning Recommendation                                                   | keyword  |
| CIKM    |   2024 | MemoCRS: Memory-enhanced Sequential Conversational Recommender Systems with Large Language Models              | keyword  |
| SIGIR   |   2022 | User-Centric Conversational Recommendation with Multi-Aspect User Modeling                                     | keyword  |
| SIGIR   |   2025 | Search-Based Interaction For Conversation Recommendation via Generative Reward Model Based Simulated User      | llm      |
| KDD     |   2022 | Adversarial Gradient Driven Exploration for Deep Click-Through Rate Prediction                                 | llm      |
| SIGIR   |   2022 | Dynamics-Aware Adaptation for Reinforcement Learning Based Cross-Domain Interactive Recommendation             | keyword  |
| CIKM    |   2024 | Reformulating Conversational Recommender Systems as Tri-Phase Offline Policy Learning                          | keyword  |
| CIKM    |   2024 | Mitigating Exposure Bias in Online Learning to Rank Recommendation: A Novel Reward Model for Cascading Bandits | keyword  |
| SIGIR   |   2023 | Contrastive State Augmentations for Reinforcement Learning-Based Recommender Systems                           | keyword  |

## Cold-start / Federated（全 299 件から無作為 20 件）

| venue   |   year | title                                                                                      | source   |
|:--------|-------:|:-------------------------------------------------------------------------------------------|:---------|
| SIGIR   |   2019 | An Efficient Adaptive Transfer Neural Network for Social-aware Recommendation              | llm      |
| SIGIR   |   2024 | Aiming at the Target: Filter Collaborative Information for Cross-Domain Recommendation     | keyword  |
| WWW     |   2023 | Cross-domain Recommendation with Behavioral Importance Perception                          | keyword  |
| CIKM    |   2022 | Tiger: Transferable Interest Graph Embedding for Domain-Level Zero-Shot Recommendation     | keyword  |
| SIGIR   |   2021 | FedCT: Federated Collaborative Transfer for Recommendation                                 | keyword  |
| RecSys  |   2019 | Domain adaptation in display advertising: an application for partner cold-start            | keyword  |
| WSDM    |   2023 | Towards Universal Cross-Domain Recommendation                                              | keyword  |
| WWW     |   2022 | Differential Private Knowledge Transfer for Privacy-Preserving Cross-Domain Recommendation | keyword  |
| WWW     |   2025 | Plug and Play: Enabling Pluggable Attribute Unlearning in Recommender Systems              | llm      |
| CIKM    |   2025 | FedSTEP: Asynchronous and Staleness-Aware Personalization for Efficient Federated Learning | keyword  |
| KDD     |   2025 | Exploring Preference-Guided Diffusion Model for Cross-Domain Recommendation                | keyword  |
| CIKM    |   2022 | Cross-Network Social User Embedding with Hybrid Differential Privacy Guarantees            | keyword  |
| CIKM    |   2024 | DAMe: Personalized Federated Social Event Detection with Dual Aggregation Mechanism        | keyword  |
| WWW     |   2024 | Co-clustering for Federated Recommender System                                             | keyword  |
| WWW     |   2025 | Achieving Personalized Privacy-Preserving Graph Neural Network via Topology Awareness      | keyword  |
| SIGIR   |   2021 | Learning Graph Meta Embeddings for Cold-Start Ads in Click-Through Rate Prediction         | keyword  |
| RecSys  |   2025 | Affect-aware Cross-Domain Recommendation for Art Therapy via Music Preference Elicitation  | keyword  |
| CIKM    |   2024 | A General Strategy Graph Collaborative Filtering for Recommendation Unlearning             | llm      |
| SIGIR   |   2020 | How to Retrain Recommender System?: A Sequential Meta-Learning Method                      | keyword  |
| WWW     |   2024 | Prompt-enhanced Federated Content Representation Learning for Cross-domain Recommendation  | keyword  |

## LLM-based（全 181 件から無作為 20 件）

| venue   |   year | title                                                                                                                | source   |
|:--------|-------:|:---------------------------------------------------------------------------------------------------------------------|:---------|
| RecSys  |   2025 | A Language Model-Based Playlist Generation Recommender System                                                        | keyword  |
| WWW     |   2024 | PMG : Personalized Multimodal Generation with Large Language Models                                                  | keyword  |
| RecSys  |   2024 | Prompt Tuning for Item Cold-start Recommendation                                                                     | keyword  |
| WWW     |   2024 | Item-side Fairness of Large Language Model-based Recommendation System                                               | keyword  |
| SIGIR   |   2025 | Search-Based Interaction For Conversation Recommendation via Generative Reward Model Based Simulated User            | llm      |
| CIKM    |   2023 | Timestamps as Prompts for Geography-Aware Location Recommendation                                                    | keyword  |
| KDD     |   2025 | Collaboration of Large Language Models and Small Recommendation Models for Device-Cloud Recommendation               | keyword  |
| WWW     |   2024 | Generative News Recommendation                                                                                       | llm      |
| RecSys  |   2024 | Instructing and Prompting Large Language Models for Explainable Cross-domain Recommendations                         | keyword  |
| WWW     |   2024 | Could Small Language Models Serve as Recommenders? Towards Data-centric Cold-start Recommendation                    | keyword  |
| SIGIR   |   2024 | Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning                                         | keyword  |
| RecSys  |   2025 | LLM-RecG: A Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation                                    | keyword  |
| SIGIR   |   2025 | Order-agnostic Identifier for Large Language Model-based Generative Recommendation                                   | keyword  |
| WWW     |   2025 | Graph Meets LLM for Review Personalization based on User Votes                                                       | keyword  |
| KDD     |   2025 | Generating Long Semantic IDs in Parallel for Recommendation                                                          | keyword  |
| WWW     |   2022 | Modality Matches Modality: Pretraining Modality-Disentangled Item Representations for Recommendation                 | keyword  |
| SIGIR   |   2024 | Reinforcement Learning-based Recommender Systems with Large Language Models for State Reward and Action Modeling     | keyword  |
| CIKM    |   2024 | ELCoRec: Enhance Language Understanding with Co-Propagation of Numerical and Categorical Features for Recommendation | llm      |
| WWW     |   2025 | A LLM-based Controllable, Scalable, Human-Involved User Simulator Framework for Conversational Recommender Systems   | keyword  |
| RecSys  |   2024 | ReLand: Integrating Large Language Models' Insights into Industrial Recommenders via a Controllable Reasoning Pool   | keyword  |

## どの軸にも該当しなかった論文（全 469 件から無作為 20 件）

古典的な協調フィルタリング、評価・再現性、システム効率化など、
8 軸のいずれにも属さない研究がここに入る。取りこぼしがないかを確認する。

| venue   |   year | title                                                                                                                 |
|:--------|-------:|:----------------------------------------------------------------------------------------------------------------------|
| RecSys  |   2020 | Towards Safety and Sustainability: Designing Local Recommendations for Post-pandemic World                            |
| WSDM    |   2021 | Beyond Point Estimate: Inferring Ensemble Prediction Variation from Neuron Activation Strength in Recommender Systems |
| RecSys  |   2019 | Users in the loop: a psychologically-informed approach to similar item retrieval                                      |
| RecSys  |   2025 | On the Reliability of Sampling Strategies in Offline Recommender Evaluation                                           |
| SIGIR   |   2019 | Noise Contrastive Estimation for One-Class Collaborative Filtering                                                    |
| KDD     |   2019 | Effective and Efficient Reuse of Past Travel Behavior for Route Recommendation                                        |
| WSDM    |   2021 | Learning User Representations with Hypercuboids for Recommender Systems                                               |
| RecSys  |   2021 | "Serving Each User": Supporting Different Eating Goals Through a Multi-List Recommender Interface                     |
| KDD     |   2022 | Towards Representation Alignment and Uniformity in Collaborative Filtering                                            |
| WWW     |   2021 | Projected Hamming Dissimilarity for Bit-Level Importance Coding in Collaborative Filtering                            |
| KDD     |   2021 | Initialization Matters: Regularizing Manifold-informed Initialization for Neural Recommendation Systems               |
| WWW     |   2023 | AutoS2AE: Automate to Regularize Sparse Shallow Autoencoders for Recommendation                                       |
| KDD     |   2021 | Table2Charts: Recommending Charts by Learning Shared Table Representations                                            |
| WSDM    |   2023 | Improving News Recommendation with Channel-Wise Dynamic Representations and Contrastive User Modeling                 |
| KDD     |   2021 | Towards a Better Understanding of Linear Models for Recommendation                                                    |
| RecSys  |   2024 | Improving the Shortest Plank: Vulnerability-Aware Adversarial Training for Robust Recommender System                  |
| RecSys  |   2020 | Neural Collaborative Filtering vs. Matrix Factorization Revisited                                                     |
| KDD     |   2022 | Knowledge-enhanced Black-box Attacks for Recommendations                                                              |
| WWW     |   2022 | Who to Watch Next: Two-side Interactive Networks for Live Broadcast Recommendation                                    |
| CIKM    |   2020 | DE-RRD: A Knowledge Distillation Framework for Recommender System                                                     |
