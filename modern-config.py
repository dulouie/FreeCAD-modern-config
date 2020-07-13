import FreeCAD

grp = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/View')
parameters = {
    "BacklightColor" : 4294967295,
    "BackgroundColor" : 4294967295,
    "BackgroundColor2" : 4294967295,
    "BackgroundColor3" : 4059430911,
    "BackgroundColor4" : 1869583359,
    "HighlightColor" : 4118348031,
    "SelectionColor" : 3462136063,
    "PickRadius" : 12.000000000000,
    "DefaultShapeColor" : 3435973887,
    "RandomColor" : True,
    "DefaultShapeLineColor" : 421075455,
    "DefaultShapeLineWidth" : 2,
    "DefaultShapeVertexColor" : 421075455,
    "DefaultShapeVertexWidth" : 2,
    "BoundingBoxColor" : 4008635647,
    "AnnotationTextColor" : 3419130879,
    "SketchEdgeColor" : 775173887,
    "SketchVertexColor" : 775173887,
    "EditedEdgeColor" : 775173887,
    "EditedVertexColor" : 775173887,
    "ConstructionColor" : 879076607,
    "ExternalColor" : 1968208895,
    "FullyConstrainedColor" : 1943148287,
    "ConstrainedIcoColor" : 775173887,
    "NonDrivingConstrDimColor" : 1923076095,
    "ConstrainedDimColor" : 541755391,
    "ExprBasedConstrDimColor" : 2404975359,
    "CursorTextColor" : 775173887,
    "CursorCrosshairColor" : 775173887,
    "CreateLineColor" : 775173887
}

def setParameter(parameter, value):
    if type(value) is int:
        grp.SetUnsigned(parameter, value)
    if type(value) is float:
        grp.SetFloat(parameter, value)
    if type(value) is bool:
        grp.SetBool(parameter, value)


for item, value in parameters.items():
    setParameter(item, value)


