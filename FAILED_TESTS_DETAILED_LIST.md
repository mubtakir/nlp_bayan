# قائمة مفصلة بالاختبارات الفاشلة
# Detailed List of Failed Tests

**التاريخ:** 2025-11-17  
**إجمالي الفاشلة:** 144 اختبار

---

## 📋 حسب الملف / By File

### 1. test_nlp_bayan_generation.py (50 اختبار) ⭐⭐⭐

```
1. test_generate_trigram_ar_basic
2. test_generate_trigram_from_docs_custom
3. test_generate_trigram_from_docs_fallback_to_bigram
4. test_generate_trigram_from_docs_fallback_break_when_bigram_empty
5. test_generate_trigram_kb_prefers_allowed_candidate
6. test_generate_trigram_kb_no_allowed_falls_back
7. test_generate_trigram_kb_entity_backoff_to_house
8. test_generate_trigram_kb_temp0_picks_top1
9. test_generate_trigram_kb_sampling_reproducible_with_seed
10. test_generate_trigram_kb_entity_backoff_student_prefers_school
11. test_generate_trigram_kb_entity_backoff_teacher_prefers_school
12. test_morpho_inserts_ila_for_mosque
13. test_morpho_inserts_ila_for_dakhal
14. test_morpho_inserts_min_for_kharaja
15. test_morpho_inserts_ila_for_aada
16. test_morpho_inserts_fi_for_jalasa
17. test_morpho_inserts_fi_for_jalasa_library
18. test_enter_prefers_indoor_over_outdoor
19. test_exit_prefers_outdoor_over_indoor
20. test_return_prefers_house_over_others
21. test_morpho_and_kb_with_new_places_restaurant
22. test_top_p_limits_to_top1_even_with_temperature
23. test_enter_prefers_university_over_beach
24. test_sit_prefers_cafe
25. test_exit_prefers_outdoor_beach_or_stadium
26. test_enter_hotel_indoor
27. test_morpho_inserts_ila_for_wasal
28. test_morpho_inserts_ila_for_tawajja
29. test_morpho_inserts_ba_for_mar
30. test_morpho_inserts_min_for_iqtaraba
31. test_morpho_inserts_an_for_ibtaada
32. test_morpho_inserts_ila_for_safara
33. test_safara_prefers_travel_place_over_mall
34. test_zara_prefers_visitable_over_airport
35. test_mar_prefers_outdoor_beach_over_hotel
36. test_kb_weighting_prefers_visitable_in_top_p
37. test_morpho_merges_ba_al_to_bal
38. test_morpho_merges_ba_al_to_bal_stadium
39. test_stop_tokens_break_after_min_length
40. test_max_length_enforced_no_morpho_insert
41. test_min_length_overrides_stop_until_reached
42. test_morpho_inserts_min_for_ghadara
43. test_istaqara_prefers_indoor_over_outdoor
44. test_haraba_prefers_outdoor_and_inserts_min
45. test_tawajjaha_inserts_ila_prefers_high_prob_go_target
46. test_empty_docs_safe_generation_go_seeded
47. test_combined_controls_no_crash_and_respect_length
48. test_raja_morphology_inserts_ila_and_picks_house_by_docs
49. test_raja_prefers_house_over_others
50. test_dialogue_generation::test_generate_with_dialogue_prefers_last_place_and_morphology
```

**الخطأ الشائع:** SyntaxError في nlp_bayan modules

---

### 2. test_ai_ml_*.py (30+ اختبار) ⭐⭐⭐

```
test_ai_ml.py:
- test_ml_linear_regression_and_knn

test_ai_ml_kfold.py:
- test_ml_kfold_indices_basic

test_ai_ml_kfold_eval.py:
- test_ml_kfold_evaluate_logistic_and_knn

test_ai_ml_kfold_generic.py:
- test_ml_kfold_cross_val_accuracy_generic

test_ai_ml_kmeanspp.py:
- test_ml_kmeans_pp_two_clusters

test_ai_ml_kmeanspp_prob.py:
- test_ml_kmeanspp_prob_clusters

test_ai_ml_metrics_split.py:
- test_ml_train_test_split_and_metrics

test_ai_ml_roc_auc_confusion.py:
- test_ml_roc_auc_and_confusion

test_ai_ml_wave13.py:
- test_ml_adaboost_and_dataset
- test_ml_adaboost_threshold_1d
- test_ml_adaboost_arabic_wrappers

test_ai_ml_wave14_nb.py:
- test_ml_naive_bayes_simple_text
- test_ml_naive_bayes_arabic_wrappers

test_ai_ml_wave16_metrics.py:
- test_ml_mcc_and_kappa_basic

test_ai_ml_wave16_stratified.py:
- test_ml_stratified_kfold_and_split

test_ai_ml_wave17_pca.py:
- test_ml_pca_basic_shapes_and_reconstruction

test_ai_ml_wave17_variance.py:
- test_ml_variance_threshold_mask_and_transform

test_ai_ml_wave18_softmax.py:
- test_softmax_shapes_and_prob_sums
- test_softmax_accuracy_and_metrics

test_ai_ml_wave19_grid.py:
- test_grid_search_cv_softmax_selects_better_params

test_ai_ml_wave19_stacking.py:
- test_stacking_softmax_meta_multiclass

test_ai_ml_wave19_voting.py:
- test_voting_hard_binary
- test_voting_soft_multiclass

test_ai_ml_wave7.py:
- test_ml_perceptron_knn_weighted_random_forest

test_ai_ml_wave8.py:
- test_ml_linear_svm_wave8

test_ai_ml_wave9.py:
- test_ml_svm_ovr_and_bagging

test_ai_ml_confusion_multiclass.py:
- test_ml_confusion_multiclass_and_report

test_ai_ml_decision_tree.py:
- test_ml_decision_tree_xor_gini_and_entropy

test_ai_kmeans.py:
- test_ml_kmeans_two_clusters

test_ai_logreg.py:
- test_ml_logistic_regression_train_and_predict
```

**الخطأ الشائع:** SyntaxError في ai/ml.bayan

---

### 3. test_ai_data_*.py (13 اختبار) ⭐⭐⭐

```
- test_data_csv_rows_and_stats
- test_data_csv_text_helpers
- test_data_json_text_array_and_object
- test_data_prng_api_repeatability_and_ops
- test_data_prng_and_shuffle_split
- test_data_median_and_percentile
- test_data_min_max_range_and_zscore
- test_data_encoders_wave10
- test_data_simple_pipeline_variance_then_pca
- test_data_minmax_and_pearson_and_arabic_wrappers
- test_data_scalers_wave8
- test_data_binning_and_one_hot
```

**الخطأ الشائع:** AttributeError في ai/data.bayan

---

### 4. test_ai_nlp_*.py (10 اختبارات) ⭐⭐

```
- test_nlp_cooccurrence_build_and_similarity
- test_nlp_lm_eval_and_pipeline_ar_en_wrappers
- test_nlp_sequence_utils_and_metrics
- test_nlp_char_ngram_vocab_and_encode
- test_nlp_vocab_build_and_encode_decode
- test_nlp_similarity_router
- test_nlp_jaro_and_winkler_known_pairs
- test_nlp_wave15_arabic_wrappers
- test_soft_tfidf_improves_similarity_with_typos
- test_soft_tfidf_identical_texts_high_similarity
```

---

### 5. test_similarity_core.py (4 اختبارات) ⭐⭐

```
- test_close_with_default_threshold
- test_close_with_explicit_tau
- test_synonym_rule_lists_pairs
- test_synset_function_adds_pairs
```

**الخطأ:** SyntaxError في similarity_core.bayan

---

### 6. test_template_match.py (3 اختبارات) ⭐⭐

```
- test_template_match_simple_ar
- test_template_match_with_regex_and_render
- test_match_str_direct_without_compile
```

---

### 7. test_match_in_as.py (3 اختبارات) ⭐⭐

```
- test_match_in_as_basic
- test_match_in_as_arabic_keywords
- test_match_in_as_english
```

---

### 8. test_list_pattern.py (3 اختبارات) ⭐

```
- test_simple_list_pattern
- test_multiple_heads_pattern
- test_mixed_pattern
```

**الخطأ:** TypeError: ListPattern

---

### 9. test_ai_vision_*.py (2 اختبار) ⭐

```
- test_vision_conv2d_valid_and_sobel
- test_vision_threshold_basic
```

---

### 10. test_temporal_constructs.py (2 اختبار) ⭐

```
- test_delay_statement_english
- test_delay_statement_arabic
```

---

### 11. اختبارات متفرقة (15+ اختبار) ⭐

```
test_operators.py:
- test_operator_go_ar

test_prob_thresholds_topk.py:
- test_maybe_likely_and_topk_prob_fallback

test_entity_engine.py:
- test_entity_engine_reaction_response
- test_perform_action_multi_actors_self_target_and_preassignments

test_entity_syntax.py:
- test_entity_apply_arabic_keywords

test_entity_syntax_unification.py:
- test_entity_arabic_new_syntax

test_cognitive_model.py:
- test_concurrent_events

test_equations.py:
- test_equation_complement_state_ar

test_define_operator.py:
- test_define_operator_ar

test_integrated_kb_selective.py:
- test_kb_load_selective_prob_only
- test_kb_load_selective_prob_and_family

test_dialogue_two_turn_state.py:
- test_two_turn_dialogue_coreference_with_kb_and_state

test_generators_execution.py:
- test_fibonacci_generator_prefix

test_bayan_cli_api.py:
- test_simple_api_basic_generation
- test_cli_demo_runs_and_returns_string

test_arabic_text_handling.py:
- test_arabic_string_operations

test_approx_eq.py:
- test_string_semantic_approx_eq_lexicon

test_collect_topk.py:
- test_collect_topk_argmax_with_similarity

test_cut.py:
- test_parse_cut_with_list_pattern

test_cut_execution.py:
- test_cut_with_list_pattern

test_ai_wave20_examples.py:
- test_wave20_softmax_multiclass_example
- test_wave20_soft_tfidf_similarity_example
- test_wave20_pipeline_example_dimension
- test_wave20_voting_example_accuracy

test_action_centric_api.py:
- test_groups_and_last_reference_ar
```

---

**المجموع:** 144 اختبار فاشل

