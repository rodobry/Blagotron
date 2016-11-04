import random
from discord.ext import commands

class Joke():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Des blagues sur les daronnes, tape la commande ci-dessous pour avoir une blague aléatoire')
    async def tamere(self):
        """French Yo Mama Jokes"""
        tamere = [
            "Ta mère est tellement grosse que pour la voir entièrement, on doit reculer de trois pas.",
            "Ta mère est tellement grosse qu'il faut deux pokéflutes pour la réveiller.",
            "Ta mère est tellement grosse qu'il y a un décalage horaire entre ses deux fesses.",
            "Ta mère est tellement radine que, quand elle vomit, elle sert les dents pour garder les morceaux.",
            "Ta mère est tellement moche que ton père est capable de l'emmener au travail pour éviter de lui dire au revoir en l'embrassant.",
            "Ta mère est tellement vieille que quand elle pète, elle fait de la poussière.",
            "Ta mère est tellement desséchée que ses morpions ne se baladent jamais sans leur gourde perso.",
            "Ta mère est tellement grosse qu'elle a décroché le rôle de la grosse pierre roulante au casting d'Indiana Jones.",
            "Ta mère est tellement grosse qu'elle a été baptisée en mer.",
            "Ta mère est tellement pauvre que ce sont les pigeons qui lui jettent du pain.",
            "Ta mère est tellement moche que quand elle va à la banque ils coupent les caméras.",
            "Ta mère est tellement grosse que quand elle met des talons aiguilles, elle trouve du pétrole !",
            "Ta mère est tellement petite que sa tête pue des pieds.",
            "Ta mère est tellement veille quel fait du lait en poudre.",
            "Ta mère a tellement mauvaise haleine qu'on a l'impression qu'elle a l'anus derrière les dents.",
            "Si tu vois un bateau qui flotte sur l'eau c'est que ta mère n'est pas à bord.",
            "Ta mère est tellement grosse que lorsqu'elle tombe du lit elle tombe des deux bords.",
            "Ta mère est tellement grosse que pour la photographier il faut un satellite.",
            "Ta mère est tellement grosse que quand elle mange des cacahuètes, elle chie des Snickers.",
            "Ta mère est tellement grosse que lorsqu'elle se pèse, c'est son numéro de téléphone qui s'affiche !",
            "Si les femmes sont des fleurs, il faudrait changer l'eau de ta mère.",
            "Ta mère est tellement bête que quand ton père l'a demandée en mariage elle a dit oui"
        ]
        print('Blague sur les daronnes')
        await self.bot.say(random.choice(tamere))

    @commands.command(description='Des petites blagues sur melon et melèche, tape la commande ci-dessous pour avoir une blague aléatoire')
    async def mm(self):
        """Blagues melon et meleche."""
        mm = [
            "Melon et Melèche vont a la pêche. Melon prend les hameçons et Melèche la gaule :joy:",
            "Melon et Melèche sont à la pêche. Melon pêche le thon et Melèche la raie :joy:",
            "Melon et Melèche achètent une vieille maison. Melon la répare et Melèche l'habite :joy:",
            "Melon et Melèche veulent débuter dans l'apiculture. Melon achète la ruche et Melèche l'essaim :joy:",
            "Melon et Melèche apprennent la navigation à voile. Melon étudie le vent, et Melèche le noeud :joy:",
            "Melon et Melèche se font attaquer par un chien. Melon lui tire les oreilles et Melèche la queue :joy:",
            "Melon et Melèche attrapent une abeille. Melon lui arrache les pattes et Melèche le dard :joy:",
            "Melon et Melèche sont au bal. Melon regarde les rockeuses et Melèche les valseuses :joy:",
            "Melon et Melèche sont à la mer et trouvent des coquillages. Melon garde la coquille et Melèche la moule :joy:",
            "Melon et Melèche sont au port. Melon regarde le bateau et Melèche la bite :joy:",
            "Melon et Melèche font l'autopsie d'une personne assassinée. Melon examine les coups de couteau et Melèche le trou de balle :joy:",
            "Melon et Melèche sont boulangers. Melon enfourne les baguettes et Melèche les miches :joy:",
            "Melon et Melèche sont a Bricomarché. Melon prend le raccord et Melèche le clou :joy:",
            "Melon et Melèche sont charcutiers. Melon prépare les filets et Melèche les rognons :joy:",
            "Melon et Melèche partagent une glace. Melon mange le cornet et Melèche les boules :joy:",
            "Melon et Melèche vont chez le poissonnier. Melon achète les sardines et Melèche la raie :joy:",
            "Melon et Melèche hissent un drapeau. Melon tient le tissu et melèche le poteau :joy:",
            "Melon et Melèche sont en forêt, au pied d'un chêne. Melon ramasse une feuille et Melèche le gland :joy:",
            "Melon et Melèche sont viticulteurs. Melon récolte le raisin et Melèche la grappe :joy:",
            "Melon et Melèche construisent un bateau. Melon travaille le bois et Melèche le jonc :joy:",
            "Melon et Melèche sont électriciens. Melon casse le fusible et Melèche l'ampoule :joy:",
            "Melon et Melèche embêtent un chien. Melon lui tire les poils et Melèche la queue :joy:",
            "Melon et Melèche pilotes de ligne. Melon surveille les instruments et Melèche le manche :joy:",
            "Melon et Melèche ont envie de se fumer un petit pet. Melon achète les feuilles et Melèche le bout :joy:",
            "Melon et Melèche arrosent les fleurs. Melon prend l’arrosoir et Melèche le tuyau :joy:",
            "Melon et Melèche fabriquent une ampoule. Melon amène le culot Melèche le plot :joy:",
            "Melon et Melèche font des filetages de boulons. Melon fait l'excentrique et Melèche le concentrique :joy:",
            "Melon et Melèche font de la mécanique. Melon place la vis et Melèche la rondelle :joy:",
            "Melon et Melèche font la vaisselle. Melon lave les assiettes et melèche les poêles :joy:",
            "Melon et Melèche jouent à la pétanque. Melon jette le cochonnet et Melèche les boules :joy:",
            "Melon et Melèche préparent le billard. Melon nettoie les boules et Melèche la queue :joy:",
            "Melon et Melèche jouent au Scrabble. Melon pioche le W et Melèche le Q :joy:",
            "Melon et melèche sont a l'animalerie. Melon prend le chat et melèche la chatte :joy:",
            "Melon et Melèche sont mariés à la même femme. Melon la saute et Melèche la trompe :joy:",
            "Melon et Melèche dorment à la belle étoile. Melon regarde les étoiles et Melèche la lune :joy:",
            "Melon et Melèche agrèssent un policier. Melon lui vole le képi et Melèche la trique :joy:",
            "Melon et melèche vont au jardin. Melon cherche les tomates et Melèche le poireau :joy:",
            "Melon et Melèche boivent l'apéro. Melon mange les gâteaux apéro et Melèche le saucisson :joy:",
            "Melon et Melèche préparent une sauce. Melon la cuisine et Melèche la goûte :joy:",
            "Melon et Melèche s'occupent du jardin. Melon fait le gazon et Melèche la fleur :joy:",
            "Melon et Melèche sont contrôleurs de train. Melon contrôle la tête et Melèche la queue :joy:",
            "Melon et Melèche entrent dans une boucherie. Melon achète la côtelette et Melèche la saucisse :joy:",
            "Melon et Melèche restaurent un vieux vélo. Melon répare le guidon et Melèche la béquille :joy:",
            "Melon et Melèche font une tarte aux pruneaux. Melon prépare la tarte et Melèche les pruneaux :joy:",
            "Melon et Melèche partagent une baguette. Melon mange la mie et Melèche le croûton :joy:",
            "Melon et Melèche s’en vont. Melon l’est plus là et Melèche l’est parti :joy:",
            "Melon et Melèche ont de grandes oreilles. Melon est lapin et Melèche lapine :joy:",
            "Melon et Melèche cherchent un mot. Melon consulte le Larousse et Melèche le Robert :joy:",
            "Melon et Melèche veulent planter un parasol. Melon apporte la toile et Melèche le piquet :joy:",
            "Melon et Melèche ont leur première relation sexuelle. Melon fait le réticent et Melèche le consentant :joy:",
            "Melon et Melèche prennent leur 4 heure. Melon mange les figues et Melèche les noix :joy:",
            "Melon et Melèche réparent un pneu. Melon le gonfle et Melèche le troue :joy:",
            "Melon et Melèche sont fans des rôles de Roger Moore. Melon aime James Bond et Melèche Le Saint :joy:",
            "Melon et Melèche s'échappent de prison. Melon force la serrure et Melèche le barreau :joy:",
            "Melon et Melèche sont à Eurodisney. Melon fait Space Mountain et Melèche encore la queue :joy:",
            "Melon et Melèche sont à l'Assemblée. Melon vote la poursuite des essais nucléaires et Melèche l'arrêt :joy:",
            "Melon et Melèche sont chausseurs. Melon vend les souliers et Melèche les bottes :joy:",
            "Melon et Melèche cueillent une fleur. Melon observe les pétales et Melèche le nectar :joy:",
            "Melon et Melèche fabriquent une tirelire. Melon fait le moule et Melèche la fente :joy:",
            "Melon et Melèche veulent faire des crêpes. Au supermarché, Melon achète la farine et Melèche les oeufs :joy:",
            "Melon et Melèche sont victimes de maladies microbiennes et parasitaires. Melon peste et poux et Melèche lepre et puces (me lèche le prépuce) :joy:",
            "Melon et Melèche vont à l'église. Melon cherche le curé et Melèche les Saints :joy:",
            "Melon et Melèche vont voter. Melon cherche l'isoloir et Melèche la fente :joy:",
            "Melon et Melèche voyagent en Angleterre. Melon visite Londres et Melèche l'Essex :joy:"
        ]
        print('Blague melon & meleche')
        await self.bot.say(random.choice(mm))


def setup(bot):
    bot.add_cog(Joke(bot))