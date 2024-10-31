# -*- coding: utf-8 -*-
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==================================================

from Autodesk.Revit.DB import*

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==================================================
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application

# Reusable Snippets
def get_selected_elements():
    """" Get selected Elements in Revit UI.
    you can provide a list of types for filter_types parameter (optionally)
    eg.
    sel_walls = get_selected_elements([walls])
    """

    selected_element_ids = uidoc.Selection.GetElementIds()
    selected_elements    = [doc.GetElement(e_id) for e_id in selected_element_ids]

# Filter selection (optionally)
    if filter_types:
        return [el for el in selected_elements if type(el) in filter_typpes]
    return selected_elements