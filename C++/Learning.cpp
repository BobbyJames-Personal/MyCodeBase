static bool running = true;

bool platformCreateWindow(int width, int height, char* title)

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>


#endif

int main() {
    platformCreateWindow(1200,720,"Test")
    while(running) {
        // Update
    }

    return 0;
}
