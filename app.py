if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cloud-storage-path",
        required=True,
        help="Cloud Storage path to store the AI Platform dataset files.",
    )
    parser.add_argument(
        "--bigquery-dataset",
        required=True,
        help="BigQuery dataset ID for the images database.",
    )
    parser.add_argument(
        "--bigquery-table",
        default="wildlife_images_metadata",
        help="BigQuery table ID for the images database.",
    )
    parser.add_argument(
        "--ai-platform-name-prefix",
        default="wildlife_classifier",
        help="Name prefix for AI Platform resources.",
    )
    parser.add_argument(
        "--min-images-per-class",
        type=int,
        default=50,
        help="Minimum number of images required per class for training.",
    )
    parser.add_argument(
        "--max-images-per-class",
        type=int,
        default=80,
        help="Maximum number of images allowed per class for training.",
    )
    parser.add_argument(
        "--budget-milli-node-hours",
        type=int,
        default=8000,
        help="Training budget, see: https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#imageclassificationmodelmetadata",
    )
    args, pipeline_args = parser.parse_known_args()

    pipeline_options = PipelineOptions(pipeline_args, save_main_session=True)
    project = pipeline_options.get_all_options().get("project")
    if not project:
        parser.error("please provide a Google Cloud project ID with --project")
    region = pipeline_options.get_all_options().get("region")
    if not region:
        parser.error("please provide a Google Cloud compute region with --region")

    run(
        project=project,
        region=region,
        cloud_storage_path=args.cloud_storage_path,
        bigquery_dataset=args.bigquery_dataset,
        bigquery_table=args.bigquery_table,
        ai_platform_name_prefix=args.ai_platform_name_prefix,
        min_images_per_class=args.min_images_per_class,
        max_images_per_class=args.max_images_per_class,
        budget_milli_node_hours=args.budget_milli_node_hours,
        pipeline_options=pipeline_options,
    )
