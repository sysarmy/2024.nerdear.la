from .DatasetsUtils import DatasetsUtils


class SponsorProcessorError(Exception):
    """Custom exception class for errors encountered during sponsor processing."""

    pass


class SponsorProcessor:
    """
    SponsorProcessor class for processing sponsors and grouping them by category.
    """

    @staticmethod
    def process_sponsors(sponsors, config):
        """
        Process the sponsors by performing various operations on the input sponsors data.

        Args:
            sponsors (list): A list of dictionaries representing the sponsors.
            config (dict): A configuration dictionary containing the category order.

        Returns:
            dict: A dictionary with the sponsors grouped by category.

        Raises:
            SponsorProcessorError: If there is an error encountered during sponsor processing.
        """
        try:
            # Get the configuration from the config file
            category_order = config.get("category_order")

            if not category_order or not isinstance(category_order, list):
                raise ValueError("Invalid or missing 'category_order' in the config.")

            # Removes trailing whitespace from the keys
            sponsors = DatasetsUtils.remove_trailing_whitespace(sponsors)
            # Convert key values to lowercase, just in case the input in the CSV is in caps
            DatasetsUtils.convert_key_values_to_lowercase(sponsors, "category")

            # Sort the sponsors by the category_order list
            sponsors = sorted(
                sponsors,
                key=lambda x: category_order.index(x["category"])
                if x["category"] in category_order
                else len(category_order),
            )

            # Convert the sponsors into a dictionary with the sponsors grouped by category
            grouped_sponsors = {}
            for sponsor in sponsors:
                category = sponsor.get("category")
                if not category:
                    raise KeyError("Missing 'category' key in a sponsor.")
                if not isinstance(category, str):
                    raise TypeError("'category' value in a sponsor is not a string.")
                if category in grouped_sponsors:
                    grouped_sponsors[category].append(sponsor)
                else:
                    grouped_sponsors[category] = [sponsor]
        except Exception as e:
            raise SponsorProcessorError(f"An error occurred while processing the sponsors: {e}")

        return grouped_sponsors
