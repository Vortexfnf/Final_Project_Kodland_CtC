import datetime
import os
import discord
import asyncio
import random
from discord.ext import commands
from ImageDetector import detect_image
import tensorflow
from PIL import Image, ImageOps

# Intents
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'The bot has logged in on discord as {client.user}')

# Ideas para ayudar contra la contamimación
ideas = [
    "Transformar botellas de plástico en PLA (hilo para impresoras 3D)",
    "Llevar plástico a centros de reciclaje locales",
    "Crear eco-ladrillos con plástico compactado",
    "Crear objetos útiles o decorativos a partir de botellas y envases plásticos",
    "Construir un invernadero pequeño utilizando botellas plásticas",
    "Usar bolsas reutilizables en lugar de bolsas plásticas de un solo uso",
    "Convertir objetos plásticos viejos en nuevos productos útiles",
    "Comprar productos con menos envases plásticos y usar contenedores recargables",
    "Informar a otros sobre la importancia del reciclaje de plástico y la reducción de su uso",
    "Utilizar plásticos biodegradables y compostarlos en lugar de desecharlos",
    "Reciclar papel y combinarlo con plástico derretido para hacer papel reciclado",
    "Cultivar tus propias frutas y verduras puede reducir el uso de envases plásticos",
    "Optar por productos reutilizables en lugar de los de un solo uso",
    "Elegir productos sin microesferas de plástico",
    "Arreglar objetos plásticos rotos en lugar de reemplazarlos",
    "Comprar productos con envases que puedan ser devueltos o rellenados",
    "Participar en limpiezas comunitarias para eliminar plásticos de entornos naturales",
    "Optar por opciones reutilizables o biodegradables",
    "Apoyar iniciativas y legislaciones locales para reducir el uso de plásticos",
    "Promover la conciencia y la acción sostenible en la comunidad",
    "Fomentar el uso de botellas de agua reutilizables",
    "Utilizar pajitas de metal o bambú en lugar de pajitas de plástico",
    "Reemplazar utensilios de plástico con alternativas de acero inoxidable o madera",
    "Evitar el uso de envoltorios de plástico al transportar alimentos",
    "Comprar productos de segunda mano en lugar de nuevos para reducir el uso de embalajes",
    "Apoyar negocios locales que utilizan envases biodegradables",
    "Crear una campaña educativa sobre el impacto del plástico en los océanos",
    "Desarrollar un programa de recolección de plásticos en áreas rurales",
    "Utilizar contenedores de vidrio en lugar de plástico para almacenar alimentos",
    "Fomentar el uso de bolsas de tela para la compra de alimentos a granel",
    "Incentivar a las empresas a adoptar prácticas de embalaje sostenibles",
    "Organizar eventos de reutilización y trueque de objetos en la comunidad",
]


@client.command()
async def Ideas(ctx):
    await ctx.send(random.choice(ideas))

@client.command()
async def Bidon(ctx, color="None"):
    async with ctx.typing():
        await asyncio.sleep(1)
    if color.upper() == "AMARILLO":
        await ctx.send("Bidón Amarillo: Para reciclar envases")
    elif color.upper() == "AZUL":
        await ctx.send("Bidón Azul: Para reciclar Papel y Cartón")
    elif color.upper() == "GRIS":
        await ctx.send("Bidón Gris: Para reciclar Papel y Cartón")
    elif color.upper() == "VERDE":
        await ctx.send("Bidón Verde: Para reciclar Vidrio")
    elif color.upper() == "ROJO":
        await ctx.send("Bidón Rojo: Para reciclar Plástico")
    elif color.upper() == "MARRON":
        await ctx.send("Bidón Marrón: Para reciclar Materia Orgánica")
    elif color.upper() == "NEGRO":
        await ctx.send("Bidón Negro: Para residuos no reciclables")
    else:
        await ctx.send("Color de Bidón no reconocido. Por favor, elija entre: Amarillo, Azul, Gris, Verde, Rojo, Marrón o Negro.")
    

@client.command(name="server_info", aliases=["serverinfo"], help="Displays information about the server.")
async def server_info(ctx):
    # Get the server information
    server = ctx.guild
    # Creating an embed
    embed = discord.Embed(title="Server Information", color=discord.Color.blue())
    
    embed = discord.Embed(title=f"Server Information - {server.name}", color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon.url)  # Use 'icon' attribute instead of 'icon_url'
    embed.add_field(name="Server's ID", value=server.id, inline=False)
    embed.add_field(name="Server owner", value=server.owner, inline=False)
    embed.add_field(name="Total member count", value=server.member_count, inline=False)
    embed.add_field(name="Text channels", value=len(server.text_channels), inline=False)
    embed.add_field(name="VC's", value=len(server.voice_channels), inline=False)
    embed.add_field(name="Roles", value=len(server.roles), inline=False)

    # Send the embed message
    async with ctx.typing():
        await asyncio.sleep(1)
    await ctx.send(embed=embed)

challenges = [
    "Use a reusable water bottle today.",
    "Pick up at least 5 pieces of trash you come across.",
    "Conserve energy by turning off lights and unplugging devices not in use.",
    "Walk, bike, or use public transport instead of driving if possible.",
    "Reduce plastic waste by avoiding single-use plastics today.",
    "Plant a tree or a plant in your backyard or a local park.",
    "Opt for paperless billing and statements for your accounts.",
    "Donate or recycle old electronics you no longer use.",
    "Switch to reusable cloth bags for groceries and shopping.",
    "Conserve water by taking shorter showers and fixing any leaks.",
    "Buy products with minimal packaging or packaging that can be recycled.",
    "Use a cloth napkin instead of disposable paper napkins.",
    "Reduce food waste by planning meals and using leftovers creatively.",
    "Switch to eco-friendly cleaning products for your home.",
    "Participate in a local beach or park cleanup event.",
    "Turn off faucets while brushing your teeth or doing dishes.",
    "Carpool with friends or colleagues to reduce vehicle emissions.",
    "Unsubscribe from unnecessary junk mail and catalogs.",
    "Make your own DIY natural air fresheners instead of using aerosols.",
    "Set up a composting system for your kitchen waste.",
    "Repair or repurpose an item instead of discarding it.",
    "Opt for digital invitations instead of paper for events.",
    "Use a refillable mug or cup for your coffee or drinks.",
    "Support local and sustainable products and businesses.",
    "Turn down your thermostat by a few degrees and wear warmer clothes.",
    "Use a reusable lunchbox or container instead of disposable ones.",
    "Avoid printing unnecessary documents and emails.",
    "Buy second-hand or vintage clothing instead of fast fashion.",
    "Contribute to an e-waste recycling program for electronics disposal.",
    "Spread awareness by sharing an environmental tip with a friend or on social media.",
    "Just Recycle. It's that easy."
]

@client.command()
async def challenge(ctx):
    # Select a random challenge from the list
    random_challenge = random.choice(challenges)
    async with ctx.typing():
        await asyncio.sleep(1)
    await ctx.send(f"🌱 Your daily challenge is: {random_challenge}")

general = "La contaminación se refiere a la introducción de sustancias, energía o agentes contaminantes en el medio ambiente, ya sea en el aire, el agua o el suelo, que causan efectos adversos en la salud humana, en los ecosistemas y en el equilibrio natural de los sistemas ambientales. Estas sustancias o agentes pueden ser productos químicos, partículas, radiación, microorganismos u otros elementos que, cuando están presentes en concentraciones superiores a las normales, generan alteraciones y daños en el entorno."

air_polution = "La contaminación del aire es la presencia en la atmósfera de sustancias nocivas en concentraciones que pueden tener efectos adversos en la salud de las personas, en el medio ambiente y en los ecosistemas. Estas sustancias contaminantes pueden ser de origen natural o humano y pueden provenir de diversas fuentes, como la quema de combustibles fósiles, la industria, la agricultura, el transporte y otras actividades humanas."

water_contamination = "La contaminación del agua se refiere a la introducción de sustancias nocivas o contaminantes en cuerpos de agua, como ríos, lagos, océanos, aguas subterráneas y otros recursos hídricos. Estas sustancias pueden alterar la calidad del agua y tener efectos adversos en los ecosistemas acuáticos, en la salud humana y en la disponibilidad de agua potable. La contaminación del agua puede ser causada por actividades humanas, naturales o una combinación de ambas."

soil_contamination = "La contaminación del suelo se refiere a la presencia de sustancias químicas, materiales o elementos tóxicos en el suelo en concentraciones que pueden ser perjudiciales para la salud humana, la vida vegetal, la fauna y el medio ambiente en general. Estos contaminantes pueden provenir de diversas fuentes, incluyendo actividades industriales, agrícolas, mineras, urbanas y otras actividades humanas. La contaminación del suelo puede tener efectos adversos a largo plazo en la calidad del suelo y en los ecosistemas que dependen de él."

sound_contamination = "La contaminación del sonido, también conocida como contaminación acústica o contaminación sonora, se refiere al exceso de ruido no deseado en el entorno que tiene efectos negativos en la salud humana, en la calidad de vida y en los ecosistemas. Este tipo de contaminación es causado por la presencia de sonidos indeseados y perturbadores que superan los niveles normales de tranquilidad en un área determinada."

light_contamination = "La contaminación lumínica, también conocida como contaminación lumínica o polución luminosa, se refiere al exceso de luz artificial en el entorno nocturno que interfiere con la observación del cielo estrellado, afecta a los ecosistemas naturales y tiene efectos negativos en la salud humana. Este tipo de contaminación se produce cuando hay una emisión excesiva de luz artificial en áreas urbanas y rurales, creando un brillo innecesario y no deseado en el cielo nocturno."

Thermal_Pollution = "Contaminación térmicase refiere a la contaminación térmica, que es el aumento de la temperatura en un cuerpo de agua, como ríos, lagos u océanos, debido a la descarga de agua caliente o caliente de fuentes industriales, de energía eléctrica o de otro tipo. Esta contaminación térmica puede tener efectos adversos en los ecosistemas acuáticos y en el medio ambiente en general."

Radioactive_Contamination = "Se refiere a la presencia no deseada de materiales radioactivos en el entorno. Estos materiales pueden provenir de actividades nucleares, accidentes en plantas nucleares, ensayos nucleares, entre otros, y pueden causar daño a la salud humana y al medio ambiente debido a la liberación de radiación ionizante."

Plastic_Pollution = "Se refiere a la acumulación y dispersión de productos plásticos en el entorno, especialmente en océanos, ríos y otros cuerpos de agua. Los plásticos pueden persistir en el medio ambiente durante mucho tiempo, causando daño a la vida marina, la fauna terrestre y afectando la cadena alimentaria."

Hazardous_Waste_Pollution = "Se refiere a la liberación inadecuada de residuos tóxicos, peligrosos o químicamente activos en el medio ambiente. Estos residuos pueden ser generados por industrias, hospitales y otros sectores, y si no se manejan adecuadamente, pueden causar impactos graves en la salud y el medio ambiente."

Biological_Contamination = "Se refiere a la introducción no deseada de microorganismos, patógenos u organismos invasores en un ecosistema. Esto puede alterar los equilibrios ecológicos y tener efectos negativos en la biodiversidad y la salud humana."

Groundwater_Contamination = "Se refiere a la contaminación de las aguas subterráneas, que son una fuente importante de agua potable. Sustancias químicas, contaminantes industriales o agrícolas pueden infiltrarse en el suelo y llegar a las aguas subterráneas, afectando la calidad del agua."

Electromagnetic_Pollution = "Se refiere a la exposición excesiva a campos electromagnéticos producidos por dispositivos electrónicos, antenas de telecomunicaciones y otros equipos. Aunque la investigación sobre sus efectos está en curso, se ha planteado preocupación sobre los posibles impactos en la salud humana."

Chemical_Spills = "Se refiere a la liberación accidental o intencionada de sustancias químicas peligrosas en el medio ambiente, como derrames de productos químicos tóxicos en tierra, agua o aire. Estos derrames pueden causar daño inmediato a la salud, la vida silvestre y el entorno."

Airborne_Allergens = "Se refiere a partículas biológicas como polen, esporas de hongos y otros alérgenos que están presentes en el aire y pueden desencadenar reacciones alérgicas en las personas susceptibles."

Acid_Rain = "Se refiere a la precipitación de lluvia con un pH más bajo de lo normal debido a la emisión de dióxido de azufre y óxidos de nitrógeno en la atmósfera. La lluvia ácida puede dañar ecosistemas acuáticos, suelos, edificios y cultivos, y contribuir a la degradación del medio ambiente."

@client.command()
async def contaminacion(ctx, type = "GENERAL"):
    async with ctx.typing():
        await asyncio.sleep(1)
    if type.upper() == "GENERAL":
        await ctx.send(general)
    if type.upper() == "AIRE":
        await ctx.send(air_polution)
    if type.upper() == "AGUA":
        await ctx.send(water_contamination)
    if type.upper() == "SUELO":
        await ctx.send(soil_contamination)
    if type.upper() == "SONIDO":
        await ctx.send(sound_contamination)
    if type.upper() == "LUZ":
        await ctx.send(light_contamination)
    if type.upper() == "TERMICO":
        await ctx.send(Thermal_Pollution)
    if type.upper() == "RADIOACTIVO":
        await ctx.send(Radioactive_Contamination)
    if type.upper() == "PLASTICO":
        await ctx.send(Plastic_Pollution)
    if type.upper() == "RESIDUOS":
        await ctx.send(Hazardous_Waste_Pollution)
    if type.upper() == "BIOLOGICO":
        await ctx.send(Biological_Contamination)
    if type.upper() == "AGUA_DEL_SUELO":
        await ctx.send(Groundwater_Contamination)
    if type.upper() == "ELECTROMAGNETICO":
        await ctx.send(Electromagnetic_Pollution)
    if type.upper() == "QUIMICO":
        await ctx.send(Chemical_Spills)
    if type.upper() == "ALERGENOS":
        await ctx.send(Airborne_Allergens)
    if type.upper() == "LLUVIA_ACIDA":
        await ctx.send(Acid_Rain)
    
General_en = "Contamination refers to the introduction of substances, energy, or contaminating agents into the environment, whether in the air, water, or soil, that cause adverse effects on human health, ecosystems, and the natural balance of environmental systems. These substances or agents can be chemicals, particles, radiation, microorganisms, or other elements that, when present in concentrations higher than normal, generate alterations and damage to the environment."

Air_Pollution_en = "Air pollution is the presence in the atmosphere of harmful substances in concentrations that can have adverse effects on people's health, the environment, and ecosystems. These contaminating substances can be of natural or human origin and can come from various sources such as the burning of fossil fuels, industry, agriculture, transportation, and other human activities."

Water_Contamination_en = "Water contamination refers to the introduction of harmful or contaminating substances into bodies of water, such as rivers, lakes, oceans, groundwater, and other water resources. These substances can alter water quality and have adverse effects on aquatic ecosystems, human health, and the availability of drinking water. Water pollution can be caused by human activities, natural processes, or a combination of both."

Soil_Contamination_en = "Soil contamination refers to the presence of toxic chemicals, materials, or elements in the soil at concentrations that can be harmful to human health, plant life, wildlife, and the environment in general. These contaminants can come from various sources, including industrial, agricultural, mining, urban, and other human activities. Soil pollution can have long-term adverse effects on soil quality and ecosystems that depend on it."

Sound_Contamination_en = "Sound pollution, also known as acoustic pollution or noise pollution, refers to the excess of unwanted noise in the environment that has negative effects on human health, quality of life, and ecosystems. This type of pollution is caused by the presence of undesired and disruptive sounds that exceed normal levels of tranquility in a given area."

Light_Contamination_en = "Light pollution, also known as light pollution or luminous pollution, refers to the excessive artificial light in the nighttime environment that interferes with the observation of the starry sky, affects natural ecosystems, and has negative effects on human health. This pollution occurs when there is an excessive emission of artificial light in urban and rural areas, creating unnecessary and unwanted brightness in the night sky."

Thermal_Pollution_en = "Thermal pollution refers to the pollution in water bodies, such as rivers, lakes, or oceans, caused by the discharge of warm or hot water from industrial, energy production, or other sources. This thermal pollution can have adverse effects on aquatic ecosystems and the environment in general."

Radioactive_Contamination_en = "Radioactive contamination refers to the unwanted presence of radioactive materials in the environment. These materials can come from nuclear activities, accidents in nuclear plants, nuclear tests, among others, and can cause harm to human health and the environment due to the release of ionizing radiation."

Plastic_Pollution_en = "Plastic pollution refers to the accumulation and dispersal of plastic products in the environment, especially in oceans, rivers, and other water bodies. Plastics can persist in the environment for a long time, causing harm to marine life, terrestrial fauna, and affecting the food chain."

Hazardous_Waste_Pollution_en = "Hazardous waste pollution refers to the inadequate release of toxic, hazardous, or chemically active waste into the environment. These wastes can be generated by industries, hospitals, and other sectors, and if not properly managed, can cause severe impacts on health and the environment."

Biological_Contamination_en = "Biological contamination refers to the unwanted introduction of microorganisms, pathogens, or invasive organisms into an ecosystem. This can disrupt ecological balances and have negative effects on biodiversity and human health."

Groundwater_Contamination_en = "Groundwater contamination refers to the pollution of groundwater, which is an important source of drinking water. Chemicals, industrial or agricultural contaminants can infiltrate the soil and reach groundwater, affecting water quality."

Electromagnetic_Pollution_en = "Electromagnetic pollution refers to excessive exposure to electromagnetic fields produced by electronic devices, telecommunications antennas, and other equipment. While research on its effects is ongoing, concerns have been raised about possible impacts on human health."

Chemical_Spills_en = "Chemical spills refer to the accidental or intentional release of hazardous chemicals into the environment, such as spills of toxic chemicals on land, water, or air. These spills can cause immediate harm to health, wildlife, and the environment."

Airborne_Allergens_en = "Airborne allergens refer to biological particles like pollen, fungal spores, and other allergens present in the air that can trigger allergic reactions in susceptible individuals."

Acid_Rain_en = "Acid rain refers to rain precipitation with a lower pH than normal due to the emission of sulfur dioxide and nitrogen oxides into the atmosphere. Acid rain can damage aquatic ecosystems, soils, buildings, crops, and contribute to environmental degradation."

@client.command()
async def contamination(ctx, Bin_type = "GENERAL"):
    message_en=""
    if Bin_type.upper() == "GENERAL":
        message_en=General_en
    if Bin_type.upper() == "AIR":
        message_en=Air_Pollution_en
    if Bin_type.upper() == "WATER":
        message_en=Water_Contamination_en
    if Bin_type.upper() == "SOIL":
        message_en=Soil_Contamination_en
    if Bin_type.upper() == "SOUND":
        message_en=Sound_Contamination_en
    if Bin_type.upper() == "LIGHT":
        message_en=Light_Contamination_en
    if Bin_type.upper() == "THERMAL":
        message_en=Thermal_Pollution_en
    if Bin_type.upper() == "RADIOACTIVE":
        message_en=Radioactive_Contamination_en
    if Bin_type.upper() == "PLASTIC":
        message_en=Plastic_Pollution_en
    if Bin_type.upper() == "WASTE":
        message_en=Hazardous_Waste_Pollution_en
    if Bin_type.upper() == "BIOLOGICAL":
        message_en=Biological_Contamination_en
    if Bin_type.upper() == "GROUNDWATER":
        message_en=Groundwater_Contamination_en
    if Bin_type.upper() == "ELECTROMAGNETIC":
        message_en=Electromagnetic_Pollution_en
    if Bin_type.upper() == "CHEMICAL":
        message_en=Chemical_Spills_en
    if Bin_type.upper() == "ALLERGENS":
        message_en=Airborne_Allergens_en
    if Bin_type.upper() == "ACID_RAIN":
        message_en=Acid_Rain_en
    async with ctx.typing():
        await asyncio.sleep(len(message_en.replace(" ", ""))*0.05)
    await ctx.send(message_en)

PlasticBottle = "you could try reusing the water bottles by filling the inside with water, emptying it, and cleaning the top so that there aren't any germs, and fill it with water. If you don't want to save it, then throw it in the red container. If you don't have containers, type '!HowCanIHelp NoBins'."
Cans = "if you've got a typical soda can, then why don't you try reusing them, of course only if you're going to use it right away, because your soda might go bland! So if you're not going to do that, try using them as storage, for small items like coins, buttons or paperclips! Or you could rinse them out and use them to organize your workspace by storing pens, markers, even smaller tools! That way, you're giving your cans a new purpose. If you're not up to doing that, you could throw them away in the bright blue bin, if you don't have recycling bins, type 'HowCanIHelp NoBins'."

NewsPapers = "you've got some newspapers, how about try to make some Paper Mache! You just need strips of newspapers and glue. First, you have to make a mold of what you want to do, and then make it thicker by using paper mache, by first making the glue (flour and water) and preparing the paper (Cutting the newspapers in small strips), then, put the glue in a small bowl, and to actually start using it, get your mold, put a strip of paper and put it in the glue, DON'T LET IT DRY, distribute the paper around the model evenly, and once you're done using all the paper, let it dry. Tadaa! You've got a paper mache mold. Fun Fact: the creator of this bot used paper mache to make a sheath for his wooden sword."


@client.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            async with ctx.typing():
                await asyncio.sleep(1)
            result = detect_image("../keras_model.h5", "../labels.txt", f"./{attachment.filename}")
            # Extracting label without unwanted characters
            label = result.replace(" ", "")
            label = label.upper().strip()  # Ensure label is uppercase and stripped of leading/trailing whitespace
            await ctx.send(label)
            if label == "WATERBOTTLE":
                await ctx.send("Looks like you have a Water Bottle and you don't know what to do with it! Then " + str(PlasticBottle))
                await ctx.send("I hope that helped!")
            elif label == "SODACAN":
                await ctx.send("So because of my current limitations, then I can't tell if it's a food can or a soda can, but " + str(Cans))

                await ctx.send("I hope that helped!")
            elif label == "NEWSPAPER(S)":
                await ctx.send("Looks like "+ str(NewsPapers))
            else:
                await ctx.send("(Label didn't match any of the expected names)")
            print(label)

    else:
        await ctx.send("You forgot to upload the image :(")

NoBins="Then go make some by buying some bins, some stickers of each type of recycling bin, of course if you have enought space, if you don't, just go to whatever bins you have in the house, put in rubbish bags of each recycling bin and put it in all of your rubbish bins. and if you have time, try to find out a way to put a sticker on them! It's a fun way of trying to help out the enviroment."

@client.command()
async def HowCanIHelp(ctx, item_type="GENERAL"):  # Changed the parameter name from type to item_type
    item_type = item_type.strip().upper()  # Convert to uppercase after stripping whitespace
    if item_type.upper() == "WATERBOTTLE":
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.send(PlasticBottle)
    elif item_type.upper() == "CAN":
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.send(Cans, "(Sorry, I couldn't find the image for cans.)")
    elif item_type.upper()=="NOBINS":
        await ctx.send(NoBins)
    elif item_type=="":
        await ctx.send()
    else:
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.send("Sorry, I couldn't understand the item type. Please specify 'WATER BOTTLE' or 'CAN'.")

# Setting the command description for the 'server_info' command
server_info.description = "This command displays detailed information about the server."

# Setting the command brief for the 'server_info' command (a shorter description for use in the default help command)
server_info.brief = "Displays server information."

# Setting the command description for the 'Ideas' command
Ideas.description = "This command gives you an idea para luchar contra la contaminación."

# Setting the command brief for the 'Ideas' command (a shorter description for use in the default help command)
Ideas.brief = "Gives an Idea."

# Setting the command description for the 'Bidon' command
Bidon.description = "This command te dice qué contiene cada bidón de reciclaje dependiendo de qué color escribes."

# Setting the command brief for the 'Bidon' command (a shorter description for use in the default help command)
Bidon.brief = "Dice que contiene cada bidón."

# Setting the command description for the 'challenge' command
challenge.description = "This command randomly chooses 1 challenge out of 30 challenges in total"

# Setting the command brief for the 'challenge' command (a shorter description for use in the default help command)
challenge.brief = "Gives you a challenge to do at home"

# Setting the command description for the 'contamination' command
contamination.description = "This command explains what contamination is and each type of contamination"

# Setting the command brief for the 'contamination' command (a shorter description for use in the default help command)

contamination.brief = "Explains contamination to you"


client.run("Use your own Token ._.")
