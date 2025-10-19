# MultiString Prompts - ComfyUI Custom Node

This is a simple but powerful custom node for ComfyUI, designed to help you manage and sequence multiple prompts from a single, clean interface.

It's ideal for workflows like sequential video generation where you need to feed a series of different prompts into your model.

## What It Does

* **5 Prompt Slots:** Provides five large, multiline text boxes for your main prompts.
* **Prefix & Suffix:** Includes two compact, single-line text boxes to add a `prefix` (like style or quality keywords) and a `suffix` to all of your prompts.
* **Enable/Disable Toggles:** You can instantly turn the `prefix` or `suffix` on or off using "true/false" dropdowns, allowing you to test prompts without deleting your keywords.
* **Smart Empty Handling:** If you leave a prompt box empty, the node is smart enough to output a completely empty string (it won't just output `prefix,suffix`).
* **List Output:** In addition to 5 individual string outputs, it provides a single `prompt_list` output. This is perfect for feeding all 5 prompts into a "Loop" or "Batch" node for a more compact workflow.

## Inputs & Outputs

### Inputs
* **`enable_prefix` (toggle):** Set to `true` to use the prefix, `false` to ignore it.
* **`enable_suffix` (toggle):** Set to `true` to use the suffix, `false` to ignore it.
* **`prefix` (string):** A single-line string added to the *beginning* of each prompt.
* **`suffix` (string):** A single-line string added to the *end* of each prompt.
* **`multi_prompt_1` - `multi_prompt_5` (string):** Five multiline text boxes for your individual prompts.

### Outputs
* **`prompt_1` - `prompt_5` (string):** The final, processed string for each corresponding prompt. (e.g., `prefix,multi_prompt_1,suffix`).
* **`prompt_list` (LIST):** A single ComfyUI list that contains all 5 processed strings.

## How to Install

1.  Navigate to your ComfyUI installation directory.
2.  Go into the `ComfyUI/custom_nodes/` folder.
3.  Create a new folder inside `custom_nodes` (e.g., `MultiStringPrompts`).
4.  Place the `multi_prompt_node.py` and `__init__.py` files inside that new folder.
5.  **Restart your ComfyUI server.**

The node will be available by right-clicking the canvas and selecting **Add Node > MyCustomNodes > MultiString Prompts**.
