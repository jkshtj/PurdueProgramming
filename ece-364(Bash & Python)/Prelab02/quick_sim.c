#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    if (argc != 4)
    {
        printf("Usage: %s <cache size> <issue width> <architecture>\n", argv[0]);
        return 1;
    }

    int cache = atoi(argv[1]);
    int issue = atoi(argv[2]);

    double CPI1 = 2.4 + 1.8/atoi(argv[1]) - atoi(argv[2])/16.0;
    double CPI2 = 2.6 + 2.2/atoi(argv[1]) - atoi(argv[2])/16.0;

    int exec1 = CPI1 * 3000;
    int exec2 = CPI2 * 3600;
    if (argv[3][0] == 'a')
    {
        printf("Simulating :AMD Opteron: with cache size:%d: and issue width:%d: results in CPI:%1.3lf: and total execution time:%d\n", cache, issue, CPI2, exec2);
    }
    else
    {
        printf("Simulating :Intel Core i7: with cache size:%d: and issue width:%d: results in CPI:%1.3lf: and total execution time:%d\n", cache, issue, CPI1, exec1);
    }
        return 0;
}
