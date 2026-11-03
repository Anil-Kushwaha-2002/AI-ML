---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:489
- loss:MultipleNegativesRankingLoss
base_model: intfloat/multilingual-e5-small
widget:
- source_sentence: 'query: Swami Sivananda did not comment on this sloka'
  sentences:
  - 'passage: स्वयमेवात्मनात्मानं वेत्थ त्वं पुरुषोत्तम |

    भूतभावन भूतेश देवदेव जगत्पते ||१०-१५||'
  - 'passage: अर्जुन उवाच |

    किं तद् ब्रह्म किमध्यात्मं किं कर्म पुरुषोत्तम |

    अधिभूतं च किं प्रोक्तमधिदैवं किमुच्यते ||८-१||'
  - 'passage: सीदन्ति मम गात्राणि मुखं च परिशुष्यति |

    वेपथुश्च शरीरे मे रोमहर्षश्च जायते ||१-२९||'
- source_sentence: 'query: Swami Sivananda did not comment on this sloka'
  sentences:
  - 'passage: न च मां तानि कर्माणि निबध्नन्ति धनञ्जय |

    उदासीनवदासीनमसक्तं तेषु कर्मसु ||९-९||'
  - 'passage: नैनं छिन्दन्ति शस्त्राणि नैनं दहति पावकः |

    न चैनं क्लेदयन्त्यापो न शोषयति मारुतः ||२-२३||'
  - 'passage: समः शत्रौ च मित्रे च तथा मानापमानयोः |

    शीतोष्णसुखदुःखेषु समः सङ्गविवर्जितः ||१२-१८||'
- source_sentence: 'query: Swami Sivananda did not comment on this sloka'
  sentences:
  - 'passage: निमित्तानि च पश्यामि विपरीतानि केशव |

    न च श्रेयोऽनुपश्यामि हत्वा स्वजनमाहवे ||१-३१||'
  - 'passage: ये त्वक्षरमनिर्देश्यमव्यक्तं पर्युपासते |

    सर्वत्रगमचिन्त्यञ्च कूटस्थमचलन्ध्रुवम् ||१२-३||'
  - 'passage: वेदाहं समतीतानि वर्तमानानि चार्जुन |

    भविष्याणि च भूतानि मां तु वेद न कश्चन ||७-२६||'
- source_sentence: 'query: Swami Sivananda did not comment on this sloka'
  sentences:
  - 'passage: कृपया परयाविष्टो विषीदन्निदमब्रवीत् |

    अर्जुन उवाच |

    दृष्ट्वेमं स्वजनं कृष्ण युयुत्सुं समुपस्थितम् ||१-२८||'
  - 'passage: कच्चिन्नोभयविभ्रष्टश्छिन्नाभ्रमिव नश्यति |

    अप्रतिष्ठो महाबाहो विमूढो ब्रह्मणः पथि ||६-३८||'
  - 'passage: भूमिरापोऽनलो वायुः खं मनो बुद्धिरेव च |

    अहंकार इतीयं मे भिन्ना प्रकृतिरष्टधा ||७-४||'
- source_sentence: 'query: Swami Sivananda did not comment on this sloka'
  sentences:
  - 'passage: श्रेयान्द्रव्यमयाद्यज्ञाज्ज्ञानयज्ञः परन्तप |

    सर्वं कर्माखिलं पार्थ ज्ञाने परिसमाप्यते ||४-३३||'
  - 'passage: मय्येव मन आधत्स्व मयि बुद्धिं निवेशय |

    निवसिष्यसि मय्येव अत ऊर्ध्वं न संशयः ||१२-८||'
  - 'passage: अवजानन्ति मां मूढा मानुषीं तनुमाश्रितम् |

    परं भावमजानन्तो मम भूतमहेश्वरम् ||९-११||'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: SentenceTransformer based on intfloat/multilingual-e5-small
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: validation
      type: validation
    metrics:
    - type: cosine_accuracy@1
      value: 1.0
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 1.0
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 1.0
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 1.0
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 1.0
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.3333333333333333
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.19999999999999998
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09999999999999999
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 1.0
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 1.0
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 1.0
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 1.0
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 1.0
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 1.0
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 1.0
      name: Cosine Map@100
---

# SentenceTransformer based on intfloat/multilingual-e5-small

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small). It maps inputs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) <!-- at revision 614241f622f53c4eeff9890bdc4f31cfecc418b3 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
queries = [
    'query: Swami Sivananda did not comment on this sloka',
]
documents = [
    'passage: श्रेयान्द्रव्यमयाद्यज्ञाज्ज्ञानयज्ञः परन्तप |\nसर्वं कर्माखिलं पार्थ ज्ञाने परिसमाप्यते ||४-३३||',
    'passage: मय्येव मन आधत्स्व मयि बुद्धिं निवेशय |\nनिवसिष्यसि मय्येव अत ऊर्ध्वं न संशयः ||१२-८||',
    'passage: अवजानन्ति मां मूढा मानुषीं तनुमाश्रितम् |\nपरं भावमजानन्तो मम भूतमहेश्वरम् ||९-११||',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 384] [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[0.1102, 0.1047, 0.0857]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `validation`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.InformationRetrievalEvaluator)

| Metric              | Value   |
|:--------------------|:--------|
| cosine_accuracy@1   | 1.0     |
| cosine_accuracy@3   | 1.0     |
| cosine_accuracy@5   | 1.0     |
| cosine_accuracy@10  | 1.0     |
| cosine_precision@1  | 1.0     |
| cosine_precision@3  | 0.3333  |
| cosine_precision@5  | 0.2     |
| cosine_precision@10 | 0.1     |
| cosine_recall@1     | 1.0     |
| cosine_recall@3     | 1.0     |
| cosine_recall@5     | 1.0     |
| cosine_recall@10    | 1.0     |
| **cosine_ndcg@10**  | **1.0** |
| cosine_mrr@10       | 1.0     |
| cosine_map@100      | 1.0     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 489 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                          | sentence_1                                                                         |
  |:---------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type     | string                                                                              | string                                                                             |
  | modality | text                                                                                | text                                                                               |
  | details  | <ul><li>min: 16 tokens</li><li>mean: 49.27 tokens</li><li>max: 103 tokens</li></ul> | <ul><li>min: 37 tokens</li><li>mean: 45.24 tokens</li><li>max: 62 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                      | sentence_1                                                                                                              |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
  | <code>query: 6.47 And among all the Yogis he who, full of faith and with his inner self merged in Me, worships Me is deemed by Me to be the most devout.</code>                                                                                                                 | <code>passage: योगिनामपि सर्वेषां मद्गतेनान्तरात्मना \|<br>श्रद्धावान्भजते यो मां स मे युक्ततमो मतः \|\|६-४७\|\|</code> |
  | <code>query: 7.11 Of the strong, I am the strength devoid of desire and attachment, and in (all) beings, I am the desire unopposed to Dharma, O Arjuna.</code>                                                                                                                  | <code>passage: बलं बलवतां चाहं कामरागविवर्जितम् \|<br>धर्माविरुद्धो भूतेषु कामोऽस्मि भरतर्षभ \|\|७-११\|\|</code>        |
  | <code>query: 2.43 Full of desires, having heaven as their goal, (they utter speech which is directed to ends) leading to new births as the result of their works, and prescribe various methods abounding in specific actions, for the attainment of pleasure and power.</code> | <code>passage: कामात्मानः स्वर्गपरा जन्मकर्मफलप्रदाम् \|<br>क्रियाविशेषबहुलां भोगैश्वर्यगतिं प्रति \|\|२-४३\|\|</code>  |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `fp16`: True
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 16
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch | Step | validation_cosine_ndcg@10 |
|:-----:|:----:|:-------------------------:|
| 1.0   | 31   | 1.0                       |


### Training Time
- **Training**: 3.8 minutes

### Framework Versions
- Python: 3.10.11
- Sentence Transformers: 6.0.1
- Transformers: 5.17.0
- PyTorch: 2.14.0+cpu
- Accelerate: 1.15.0
- Datasets: 5.0.1
- Tokenizers: 0.23.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->