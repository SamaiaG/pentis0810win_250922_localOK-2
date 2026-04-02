#include <iostream>
#include <vector>
#include <random>

// ... (eventuell weitere Header, z.B. für Bildverarbeitung)

struct Pixel {
    unsigned char r, g, b;
};

class StoneImage {
public:
    StoneImage(int width, int height) : width(width), height(height) {
        pixels.resize(width * height);
        generateStone();
    }

    void generateStone() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(0.0, 1.0);

        for (int y = 0; y < height; y += 2) {
            for (int x = 0; x < width; x += 2) {
                if (dis(gen) >= 0.2) {
                    // Füge einen 2x2 Block hinzu
                    for (int dy = 0; dy < 2; ++dy) {
                        for (int dx = 0; dx < 2; ++dx) {
                            setPixel(x + dx, y + dy, {100, 100, 100}); // Beispielfarbe
                        }
                    }
                }
            }
        }
    }

    void setPixel(int x, int y, const Pixel& color) {
        if (x >= 0 && x < width && y >= 0 && y < height) {
            pixels[y * width + x] = color;
        }
    }

    // ... (Funktionen zum Speichern des Bildes, z.B. als PPM oder PNG)

private:
    int width, height;
    std::vector<Pixel> pixels;
};

int main() {
    StoneImage stone(256, 256);
    stone.generateStone();

    // Speichere das Bild (hier ein Platzhalter)
    stone.saveAsPPM("stone.ppm");

    return 0;
}