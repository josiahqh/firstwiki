# Signal Flow

How everything connects — from source to your ears.

---

## Analogue Input Path

```
Instrument / Mic
     │
     ▼
[Preamp / Interface Input]   ← Gain knob here
     │
     ▼
[ADC — Analogue to Digital]
     │
     ▼
[DAW — Software]
     │
     ├──► [Recording track]
     └──► [Monitor mix] → [DAC] → [Mixer] → [Speakers / Headphones]
```

## MIDI Path

```
MIDI Controller (USB)
     │
     ▼
[DAW — MIDI track]
     │
     ▼
[Software instrument] → [Audio output → Monitor mix]
```

## Full Session Chain

| Source | Connection | Into | Out to |
|--------|-----------|------|--------|
| Vocal mic | XLR | Interface input 1 | DAW channel 1 |
| Acoustic guitar | ¼" jack | Interface input 2 | DAW channel 2 |
| Keys (audio) | Stereo TRS | Interface inputs 3/4 | DAW channel 3 |
| MIDI controller | USB | DAW MIDI track | Software instrument |
| DAW master out | Interface playback | Mixer 1/2 | Speakers + headphones |

---

**Notes:**
- **Phantom power (48V):** supplies power to condenser mics via XLR. Off for ribbon mics — it will damage them.
- **Direct monitoring:** hearing your input directly from the interface has near-zero latency — use this when tracking.

**Back to:** [[Reference]]
