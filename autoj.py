import os
import sys

nombre = sys.argv
WORKSPACE = "C:/Users/MSI/eclipse-workspace/"

print(nombre[1])


def cambioDir(dirs):
    try:
        os.chdir(dirs)
    except OSError:
        print(f"->x ERROR: .settings {OSError}")


def crearDirectorio(nombreDir):
    try:
        if os.path.isdir(nombreDir) != True:
            os.mkdir(nombreDir)
            print(f"->o Directorio {nombreDir} Creado!")
        else:
            print(f"->w WARNING: Directorio {nombreDir} Existente!")
    except OSError:
        print(f"->x ERROR: {OSError}")


def crearFichero(nombreFich, dato):
    try:
        if os.path.isfile(nombreFich) != True:
            archivo = open(nombreFich, "w")
            archivo.write(dato)
            archivo.close()
            print(f"->o Archivo {nombreFich} Creado!")
        else:
            print(f"->w WARNING: Archivo {nombreFich} Existente!")
    except OSError:
        print(f"->x ERROR: {OSError}")


cambioDir(WORKSPACE)

crearDirectorio(nombre[1].capitalize())

cambioDir(nombre[1].capitalize())


crearDirectorio(".settings")

cambioDir(".settings")

prefs = """eclipse.preferences.version=1
org.eclipse.jdt.core.compiler.codegen.inlineJsrBytecode=enabled
org.eclipse.jdt.core.compiler.codegen.targetPlatform=13
org.eclipse.jdt.core.compiler.codegen.unusedLocal=preserve
org.eclipse.jdt.core.compiler.compliance=13
org.eclipse.jdt.core.compiler.debug.lineNumber=generate
org.eclipse.jdt.core.compiler.debug.localVariable=generate
org.eclipse.jdt.core.compiler.debug.sourceFile=generate
org.eclipse.jdt.core.compiler.problem.assertIdentifier=error
org.eclipse.jdt.core.compiler.problem.enablePreviewFeatures=disabled
org.eclipse.jdt.core.compiler.problem.enumIdentifier=error
org.eclipse.jdt.core.compiler.problem.reportPreviewFeatures=warning
org.eclipse.jdt.core.compiler.release=enabled
org.eclipse.jdt.core.compiler.source=13
"""

crearFichero("org.eclipse.jdt.core.prefs", prefs)

cambioDir("../")


classpath = """<?xml version="1.0" encoding="UTF-8"?>
<classpath>
	<classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-13">
		<attributes>
			<attribute name="module" value="true"/>
		</attributes>
	</classpathentry>
	<classpathentry kind="src" path="src"/>
	<classpathentry kind="output" path="bin"/>
</classpath>
"""

crearFichero(".classpath", classpath)

project = f"""<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
	<name>{nombre[1]}</name>
	<comment></comment>
	<projects>
	</projects>
	<buildSpec>
		<buildCommand>
			<name>org.eclipse.jdt.core.javabuilder</name>
			<arguments>
			</arguments>
		</buildCommand>
	</buildSpec>
	<natures>
		<nature>org.eclipse.jdt.core.javanature</nature>
	</natures>
</projectDescription>
"""

crearFichero(".project", project)

crearDirectorio("bin")

crearDirectorio("src")

cambioDir("src/")

crearDirectorio("pckg")

cambioDir("pckg/")


mainJ = """package pckg;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated by https://twitter.com/alexupps python script

	}

}
"""

crearFichero("Main.java", mainJ)
