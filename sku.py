from pyscript import document

# 2-letter code for each GUTS Tour ticket type, so every SKU is exactly 8 characters
CATEGORY_CODES = {
    "General Audience": "GA",
    "Premium": "PR",
    "VIP": "VP",
}

category_input = document.getElementById("category")
name_input = document.getElementById("product-name")
quantity_input = document.getElementById("quantity")
error_box = document.getElementById("sku-error")
result_box = document.getElementById("sku-result")


def click(event):
    error_box.textContent = ""

    category = category_input.value
    # keep only letters and digits, in capitals
    name = "".join(c for c in name_input.value.upper() if c.isalnum())
    quantity_text = quantity_input.value.strip()

    if name == "" or quantity_text == "":
        error_box.textContent = "Enter a show name and a stock quantity."
        return

    try:
        quantity = int(quantity_text)
    except ValueError:
        error_box.textContent = "Quantity must be a whole number."
        return

    if quantity < 0 or quantity > 999:
        error_box.textContent = "Quantity must be between 0 and 999."
        return

    # category (2) + name (3) + quantity (3) = 8 characters
    sku = CATEGORY_CODES[category] + name[0:3].ljust(3, "X") + str(quantity).zfill(3)

    result_box.innerHTML = (
        '<p class="k">Your SKU</p>'
        '<p class="code">' + sku + "</p>"
        '<p class="k">' + str(len(sku)) + " characters</p>"
    )
