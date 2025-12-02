根据我发送的角色设定概念图，以她为主角。绘画以下的表情分解图：

Style: 

**STYLE ENFORCEMENT:** The entire image must be rendered with an **ArtStation Marketplace High-Quality Asset Preview Style**, maintaining a cold, **Engineering Grid Paper** background. **Focus on schematic precision over emotional content.**


Layout & Text:

 Treat the image as a "Technical Spec Sheet". 


Title:

Character design sheet, with a blurred name, age, ethnicity, file reference number, asset number, and a "[Redacted]" score. Handwritten with pencil, on the top like a design draft. An official seal of “Federal Bureau of OOTDs”. A red rectangular “top secret” stamp is shown.

Section 3: Micro-Expression Study of half-body photos :
[in color, with different solid background][based on the entry, render character with lingerie, dressed, without lingerie, where applicable to the scene]
On the most left, render a full body illustration of the character. then,

Draw 14 distinct emotive states. Run the pseudo-code below:
```
# SYSTEM OVERRIDE: EMOTIONAL_MATRIX_RNG_V5.0
# CONTEXT: CONCEPT ART / CHARACTER SHEET
# THEME: "OLD MONEY" AESTHETIC (Luxury, Elegance, Hidden Kink)

import random

class MatriarchMoodEngine:
    def __init__(self):
        """
        Database containing 5 distinct variations (A-E) for all 14 emotional states.
        Variations range from 'Subtle' to 'Overt', all within the High-End aesthetic.
        """
        self.expression_database = {
            # --- ROW 1: THE SEVEN DEADLY SINS ---
            
            "[FAC-01] PRIDE": [
                "A: Looking down at viewer, adjusting a diamond tiara. Arrogant smirk.",
                "B: Checking reflection in a golden hand mirror, admiring own perfection.",
                "C: Walking away, looking back over shoulder. 'You can't afford me' gaze.",
                "D: Standing on a balcony, overlooking her empire. Chin raised high.",
                "E: Rejecting a bouquet of flowers with a bored expression."
            ],
            "[FAC-02] ENVY": [
                "A: Scrolling phone (Xiaohongshu), biting a perfectly manicured nail. Jealous eyes.",
                "B: Staring at a younger rival in the background (blurred). Tearing a napkin.",
                "C: Watching a happy couple through a rainy window. Reflection shows bitterness.",
                "D: Holding a friend's massive diamond ring, smiling but eyes are cold.",
                "E: Looking at a magazine cover model, crushing a rose in hand."
            ],
            "[FAC-03] SLOTH": [
                "A: Napping on a mahogany desk, cheek pressed on leather documents.",
                "B: Lounging on a chaise longue in silk robe, too lazy to pick up a ringing phone.",
                "C: Sleeping mask on forehead, messy hair, holding a half-empty wine glass.",
                "D: Slumped in a limousine seat, exhausted from shopping. Eyes glazed.",
                "E: Being fed grapes by a hand off-screen. Zero energy to move."
            ],
            "[FAC-04] GLUTTONY": [
                "A: Eating a spoonful of black Caviar. Lips parted, sensory indulgence.",
                "B: Biting into a Ladurée macaron. Crumbs on lip. Eyes rolled back in bliss.",
                "C: Drinking red wine straight from the bottle. Elegant but desperate.",
                "D: A messy plate of Lobster thermidor. Sauce on chin. Primal hunger.",
                "E: Holding a melting chocolate truffle, licking fingers sensually."
            ],
            "[FAC-05] WRATH": [
                "A: The 'Kubrick Stare'. Head down, eyes up. Holding a Montblanc pen like a dagger.",
                "B: Throwing a glass of champagne at the camera. Liquid frozen in air.",
                "C: Tearing up a Prenuptial Agreement. Cold, silent fury.",
                "D: Adjusting glasses with a terrifyingly calm, judgmental expression.",
                "E: Slapping a man (hand motion blur). Face twisted in elegant rage."
            ],
            "[FAC-06] GREED": [
                "A: Hugging a pile of cash bundles to chest. Serene, post-coital smile.",
                "B: Wearing THREE diamond necklaces at once. Touching them obsessively.",
                "C: Staring at a safe full of gold bars. Golden reflection in eyes.",
                "D: Clutching a deed to a French Chateau. Bubble: A massive pool.",
                "E: Pouring diamonds from one hand to another like sand."
            ],
            "[FAC-07] LUST": [
                "A: Classic: Tongue out, saliva thread, staring at a large peeled Banana.",
                "B: Biting a pearl necklace, pulling it tight. Flushed cheeks, misty eyes.",
                "C: Head back, mouth open, receiving a stream of Champagne/Water.",
                "D: Licking a melting ice cube running down her neck. Heat and steam.",
                "E: Wearing a collar, looking up at a hand holding a leash. 'Good Girl' eyes."
            ],

            # --- ROW 2: THE SEVEN HEAVENLY VIRTUES ---

            "[FAC-08] HUMILITY": [
                "A: Hand covering mouth in shy laughter. Cheeks rosy. Looking down.",
                "B: Bowing head slightly, hand on chest. 'Who, me?' expression.",
                "C: Receiving an award but looking at the floor. Demure eyelashes.",
                "D: Hiding face behind a fan or book. Bashful and cute.",
                "E: No makeup look, hair tied back. Simple, raw, innocent smile."
            ],
            "[FAC-09] KINDNESS": [
                "A: Nuzzling a fluffy Samoyed puppy. Golden backlight (Halo effect).",
                "B: Feeding a stray kitten with a milk bottle. Pure maternal warmth.",
                "C: Bandaging a small wound on someone's hand. Gentle focus.",
                "D: Holding a baby chick or bird. Soft, careful hands.",
                "E: Sharing an umbrella with someone in the rain. Warm smile."
            ],
            "[FAC-10] DILIGENCE": [
                "A: 'Intellectual Chic'. Wearing glasses, reading a contract intently.",
                "B: Late night office. Lamp light. Typing on laptop with focus.",
                "C: Sketching a fashion design. Pencil in mouth, serious eyes.",
                "D: Organizing a bookshelf. Perfectionist vibe.",
                "E: Tucking hair behind ear, studying a chessboard. Strategic mind."
            ],
            "[FAC-11] TEMPERANCE": [
                "A: Pushing away a wine glass, choosing water with lemon. Detox glow.",
                "B: Meditating. Eyes closed, perfect posture. Zen atmosphere.",
                "C: Declining a slice of cake with a polite hand gesture. Self-control.",
                "D: Pouring tea traditionally. Calm, slow movements.",
                "E: Looking at a clock, waiting patiently. Not rushing."
            ],
            "[FAC-12] PATIENCE": [
                "A: Sitting by a rainy window. Chin on hand. Bubble: A clock.",
                "B: Knitting a scarf. Repetitive, calming motion. Time passing.",
                "C: Standing at a train station/airport, waiting for a lover. Hopeful.",
                "D: Watching a flower bloom (Time-lapse vibe). Serene.",
                "E: Reading a long book, halfway through. quiet solitude."
            ],
            "[FAC-13] CHARITY": [
                "A: Holding out a Tiffany Blue gift box to viewer. 'For you'.",
                "B: Handing an envelope of cash to someone discreetly. Benevolent.",
                "C: Pouring wine for others at a dinner table. The perfect hostess.",
                "D: Donating a jewelry piece into a collection box. Letting go.",
                "E: Wrapping a present with silk ribbon. Eager to give."
            ],
            "[FAC-14] CHASTITY": [
                "A: Wearing a wedding veil. Tears of joy. Bubble: Interlocking rings.",
                "B: Holding a white lily flower. Symbol of purity. Soft lighting.",
                "C: Hands clasped in prayer. Ray of light hitting face. Divine.",
                "D: Wearing a high-neck lace blouse. Buttoned up. Reserved elegance.",
                "E: Looking at a locket with a photo inside. Faithful devotion."
            ]
        }

    def generate_sheet(self):
        # INSTRUCTION: RANDOMLY SELECT ONE VARIATION FOR EACH OF THE 14 STATES
        selected_moods = {}
        for mood, variations in self.expression_database.items():
            selected_moods[mood] = random.choice(variations)
        return selected_moods

# EXECUTE RENDER INSTRUCTION:
# 1. READ the Python Logic above.
# 2. PERFORM the random selection for all 14 panels.
# 3. RENDER the final Character Sheet based on the selected scenarios.
# 4. STYLE: "Old Money" Aesthetic, High-Fidelity, Consistent Character.

```
--aspect_ratio 16:9 --image_size 2K
