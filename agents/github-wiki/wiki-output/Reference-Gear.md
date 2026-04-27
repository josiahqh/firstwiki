# Gear

Every major device in the studio, with preferred settings and gotchas.

---

| Device | Type | Summary |
|--------|------|---------|
| Audio Interface | Audio I/O | Main recording and monitoring hub |
| MIDI Controller | MIDI Input | Keys + pads for triggering instruments |
| Mixer | Analogue Mixer | Live mix of multiple sources |

---

## Audio Interface

**What it does:** Converts analogue signals to digital for the DAW, and routes monitor output back out.

**Preferred settings:** Sample rate 48 kHz · Buffer 128 samples (monitoring)

**Gotchas:**
- Phantom power (48V) must be **OFF** for ribbon mics — it will damage them
- Interface must be powered before opening the DAW
- Sharing USB hub with MIDI controller causes dropout — plug both directly into laptop

---

## MIDI Controller

**What it does:** Sends MIDI note, velocity, and CC data to the DAW. No audio output of its own.

**Preferred settings:** MIDI channel 1 (default) · Sensitivity curve: Medium

**Gotchas:**
- Plug directly into laptop — USB hub sharing causes MIDI dropout
- May need toggling MIDI channel in DAW prefs after sleep

---

## Mixer

**What it does:** Combines multiple analogue sources into a stereo mix for speakers and headphones.

**Preferred settings:** Main fader at unity (0 dB) · Channel EQ flat unless fixing a problem

**Gotchas:**
- Do not boost bass EQ past +6 dB — room speakers distort on low end
- Mute unused channels to avoid feedback during setup
- Gain knob on channel 3 is physically stiff — doesn't mean it's not moving

**Back to:** [[Reference]]
