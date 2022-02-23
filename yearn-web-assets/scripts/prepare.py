import os

tokensFolder = "../icons/multichain-tokens/"

def writeSVG(sourceFileName, dirDestination):
	source = open(sourceFileName,"r")
	os.makedirs(dirDestination, exist_ok=True)
	dest = open(dirDestination + '/TokenSVG.js', 'w')
	dest.write("import React from 'react';\n\n")
	dest.write("function Icon(props) {\n")
	dest.write("  return (\n")
	lines = source.readlines()
	for line in lines:
		if (line.startswith("<svg")):
			line = line.replace("<svg","<svg {...props}")
		line = line.replace("clip-rule", "clipRule")
		line = line.replace("fill-rule", "fillRule")
		line = line.replace("stroke-linejoin", "strokeLinejoin")
		line = line.replace("stop-color", "stopColor")
		line = line.replace("stroke-width", "strokeWidth")
		dest.write("  " + line)
	dest.write("  )\n")
	dest.write("}\n\n")
	dest.write("export default Icon;")
	dest.close()
	source.close()

def writeImage(src, address, dirDestination, size):
	os.makedirs(dirDestination, exist_ok=True)
	dest = open(dirDestination + '/TokenImage'+size+'.js', 'w')
	dest.write("import React from 'react';\n\n")
	dest.write("function Image(props) {\n")
	dest.write("\treturn (\n")
	dest.write("\t\t<img\n\t\t\tstyle={{width: "+size+", height: "+size+"}}\n\t\t\tsrc={'https://raw.githubusercontent.com/yearn/yearn-assets/master/icons/multichain-tokens/"+src+"'}\n\t\t\talt={'"+address+"'}\n\t\t\twidth={"+size+"}\n\t\t\theight={"+size+"}\n\t\t\tloading={'eager'}\n\t\t\t{...props}/>\n")
	dest.write("\t)\n")
	dest.write("}\n\n")
	dest.write("export default Image;")
	dest.close()

for dirpath, dirnames, filenames in os.walk(tokensFolder):
	for path_image in filenames:
		hasImage32 = False
		hasImage128 = False
		hasSVG = False
		splittedPath = dirpath.split('/')
		tokenChain = splittedPath[3]
		tokenAddress = splittedPath[4]
		if (path_image.endswith('svg')):
			writeSVG(os.path.join(dirpath, path_image), "./src/tokens/" + tokenChain + "/" + tokenAddress)
			hasSVG = True
		if (path_image.endswith('32.png')):
			writeImage(
				tokenChain + "/" + tokenAddress + "/" + path_image,
				tokenAddress,
				"./src/tokens/" + tokenChain + "/" + tokenAddress,
				'32'
			)
			hasImage32 = True
		if (path_image.endswith('128.png')):
			writeImage(
				tokenChain + "/" + tokenAddress + "/" + path_image,
				tokenAddress,
				"./src/tokens/" + tokenChain + "/" + tokenAddress,
				'128'
			)
			hasImage128 = True
