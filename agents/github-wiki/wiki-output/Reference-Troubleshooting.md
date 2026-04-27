# Troubleshooting

Common problems we've already solved. Add a new section when you fix something new.

---

## No Sound at All

- Is the interface powered on and recognised by the OS? (System Preferences → Sound)
- Is the correct interface selected in DAW preferences?
- Are monitors or headphones plugged in and at non-zero volume?
- Is the DAW output channel muted?

## Latency / Audio is Delayed

**Cause:** Buffer size too large.  
**Fix:** Lower buffer size to 128 samples in DAW audio preferences.

## MIDI Dropout / Keys Stop Responding

**Cause (99%):** USB hub contention — interface and MIDI controller sharing a hub.  
**Fix:** Plug both directly into separate USB ports on the laptop.

## Feedback Loop (Loud Screech)

**Cause:** Mic input routed back through monitors.  
**Fix (immediately):** Mute the monitors or the mic channel.  
**Prevention:** Use headphones when recording with a live mic.

## Crackling / Glitchy Audio

**Cause A:** Buffer underrun (CPU can't keep up) → increase buffer to 256.  
**Cause B:** Faulty cable → swap the cable.  
**Cause C:** USB power issue → use external power supply if available.

## Interface Not Recognised After Sleep

**Fix:** Unplug and replug the interface USB. Quit and reopen the DAW. This is a known macOS/USB issue — no permanent fix.

## USB Audio Device Conflicts

**Symptom:** Random crackling or the interface switching sample rates mid-session.  
**Fix:** In macOS Audio MIDI Setup, ensure all USB audio devices are set to the same sample rate (48 kHz).

**Back to:** [[Reference]]
