import os
os.add_dll_directory("C:\\Program Files\\SciTools\\bin\\pc-win64\\") 
import understand
understand.version()
db = understand.open("XPSP1.udb")

#print(understand.Metric.list())
        
total_metrics = [ 
        "AvgCountLine","AvgCountLineBlank","AvgCountLineBlankWithInactive","AvgCountLineCode","AvgCountLineCodeWithInactive", 
        "AvgCountLineComment","AvgCountLineCommentWithInactive","AvgCyclomatic","AvgCyclomaticModified","AvgCyclomaticStrict",
        "AvgCyclomaticStrictModified","AvgEssential", "AvgEssentialStrictModified","CountClassBase", "CountClassCoupled",
        "CountClassCoupledModified","CountClassDerived","CountDeclClass","CountDeclClassMethod","CountDeclClassVariable",
        "CountDeclExecutableUnit","CountDeclFile","CountDeclFileCode","CountDeclFileHeader","CountDeclFunction","CountDeclInstanceMethod",
        "CountDeclInstanceVariable","CountDeclInstanceVariableInternal","CountDeclInstanceVariablePrivate","CountDeclInstanceVariableProtected",
        "CountDeclInstanceVariableProtectedInternal","CountDeclInstanceVariablePublic","CountDeclMethod","CountDeclMethodAll",
        "CountDeclMethodConst", "CountDeclMethodDefault","CountDeclMethodFriend", "CountDeclMethodInternal", "CountDeclMethodPrivate",
        "CountDeclMethodProtected","CountDeclMethodProtectedInternal","CountDeclMethodPublic","CountInput","CountLine", "CountLineBlank",
        "CountLineBlankWithInactive","CountLineCode","CountLineCodeDecl","CountLineCodeExe", "CountLineCodeWithInactive","CountLineComment",
        "CountLineCommentWithInactive","CountLineInactive", "CountLinePreprocessor","CountOutput","CountPath","CountSemicolon","CountStmt",
        "CountStmtDecl","CountStmtEmpty","CountStmtExe", "Cyclomatic","CyclomaticModified","CyclomaticStrict","CyclomaticStrictModified",
        "Essential","Knots","MaxCyclomatic","MaxCyclomaticModified","MaxCyclomaticStrict","MaxCyclomaticStrictModified", "MaxEssential",
        "MaxEssentialKnots","MaxInheritanceTree","MaxNesting","MinEssentialKnots","PercentLackOfCohesion","RatioCommentToCode",
        "SumCyclomatic", "SumCyclomaticModified", "SumCyclomaticStrict", "SumCyclomaticStrictModified", "SumEssential", "SumEssentialStrictModified"] 

# Calculate and save the desired metrics
with open("metricas.csv", "a") as archivo:
    archivo.truncate(0)
    metrics = db.metric(total_metrics)
    for k,v in sorted(metrics.items()):
      with open("metricas.txt", "a") as archivo:
        linea = f"{k} , {v}\n"
        archivo.write(linea)
      
      print (k,"=",v)

db.close()

# fix_me_comments = 0
# to_do_comments = 0
# for file in db.ents("file"):
#     comments = file.ents("comment")
#     for comment in comments:
#         if "fix me" in comment.comment().lower():
#             fix_me_comments += 1
#         if "to do" in comment.comment().lower():
#             to_do_comments += 1

# print("Fix me comments:", fix_me_comments)
# print("To do comments:", to_do_comments)






