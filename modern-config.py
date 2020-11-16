import FreeCAD
import os.path
from shutil import copyfile

def backupConfig():
    userDir = FreeCAD.getUserAppDataDir()
    src = userDir + "user.cfg"
    des = userDir + "user_backup.cfg"
    if(not os.path.isfile(des)):
        copyfile(src, des)
        print("Backup created on " + des)
    else:
        print("Backup already exist")

def setParameter(group, parameter, value):
    if type(value) is int:
        if value > 255:
            group.SetUnsigned(parameter, value)
        else:
            group.SetInt(parameter, value)
    elif type(value) is float:
        group.SetFloat(parameter, value)
    elif type(value) is bool:
        group.SetBool(parameter, value)
    elif type(value) is str: 
        group.SetString(parameter, value)

dictionary = {
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/View'):
    {
        "BacklightColor" : 4294967295,
        "BackgroundColor" : 4294967295,
        "BackgroundColor2" : 4294967295,
        "BackgroundColor3" : 4059430911,
        "BackgroundColor4" : 1869583359,
        "HighlightColor" : 4118348031,
        "SelectionColor" : 3462136063,
        "PickRadius" : 12.0,
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
        "CreateLineColor" : 775173887,
        "AntiAliasing" : 4,
        "UseVBO" : True,

    },
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Mod/Part') : {"MeshDeviation" : 0.2},
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Mod/Mesh') : {"MaxDeviationExport" : 0.02},
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/TreeView') : {"Enabled" : True},
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/PropertyView') : {"Enabled" : False},
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/DAGView') : {"Enabled" : False},
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/ComboView') : {"Enabled" : False},
    FreeCAD.ParamGet('User parameter:BaseApp/MainWindow/DockWindows') :
    {
        "Std_ReportView" : False,
        "Std_SelectionView" : False,
        "Std_ComboView" : True,
        "Std_PythonView" : False,
        "Std_TreeView" : True,
        "Std_PropertyView" : False,
        "Std_ReportView" : False
    },
    FreeCAD.ParamGet('User parameter:BaseApp/MainWindow/Toolbars') :
    {
        "File" : False,
        "Workbench" : True,
        "Macro" : False,
        "View" : False,
        "Structure" : True,
        "Navigation" : False,
        "Part Design Modeling" : True,
        "Part Design Helper" : True,
        "Sketcher" : True,
        "Sketcher geometries" : True,
        "Sketcher constraints" : True,
        "Sketcher tools" : False,
        "Sketcher B-spline tools" : False,
        "Sketcher virtual space" : False
    },
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/MainWindow') : {"StyleSheet" : "Light-blue.qss"},
    FreeCAD.ParamGet('User parameter:BaseApp/Preferences/General') :
    {
        "AutoloadModule" : "PartDesignWorkbench",
        "Language" : "English"
    }
}

# Toolbar placement left side
# temporary excluded
toolbar = {
    FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/PartDesignWorkbench') :
    {
        "Saved" : True,
        "Top" : "Workbench",
        "Left" : "Break,Structure,Part Design Helper,Break,Part Design Modeling",
        "Right" : "",
        "Bottom" : ""
    },
    FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/SketcherWorkbench') :
    {
        "Saved" : True,
        "Top" : "Workbench,Sketcher,Sketcher tools,Sketcher B-spline tools,Sketcher virtual space",
        "Left" : "Break,Structure,Sketcher geometries,Break,Sketcher constraints",
        "Right" : "",
        "Bottom" : ""
    }
}

backupConfig()
for group, items in dictionary.items():
    for key in items:
        setParameter(group, key, items[key])
print("New parameters written")