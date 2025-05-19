import random

class Perlin:
    def __init__(self, seed=None):
        self.gradients = []
        self.lowerBound = 0
        self.rng = random.Random(seed)  # Use a dedicated RNG for reproducibility

    def valueAt(self, t):
        if t < self.lowerBound:
            print("ERROR: Input parameter out of bounds!")
            return None
        # Add to gradients until it covers t
        while t >= len(self.gradients) - 1 + self.lowerBound:
            self.gradients.append(self.rng.uniform(-1, 1))

        discarded = int(self.lowerBound)
        d1 = t - (t // 1)
        d2 = d1 - 1
        a1 = self.gradients[int(t // 1) - discarded] * d1
        a2 = self.gradients[int(t // 1 + 1) - discarded] * d2

        amt = self.__ease(d1)
        return self.__lerp(a1, a2, amt)

    def discard(self, amount):
        gradientsToDiscard = int(amount + self.lowerBound % 1)
        self.gradients = self.gradients[gradientsToDiscard:]
        self.lowerBound += amount

    def __ease(self, x):
        return 6 * x**5 - 15 * x**4 + 10 * x**3

    def __lerp(self, start, stop, amt):
        return amt * (stop - start) + start

def perlin_multi_octave(perlin, t, octaves=4, persistence=0.5, lacunarity=2.0):
    """
    Generate multi-octave Perlin noise using a Perlin instance.
    - perlin: an instance of Perlin
    - t: time or position
    - octaves: number of octaves (layers)
    - persistence: amplitude multiplier per octave
    - lacunarity: frequency multiplier per octave
    """
    value = 0.0
    amplitude = 1.0
    frequency = 1.0
    max_amplitude = 0.0
    for _ in range(octaves):
        value += perlin.valueAt(t * frequency) * amplitude
        max_amplitude += amplitude
        amplitude *= persistence
        frequency *= lacunarity
    return value / max_amplitude if max_amplitude != 0 else 0.0