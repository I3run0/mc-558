#include "shortest_path.hpp"

using namespace std;

int main()
{

    int Q, n;

    cin >> n;
    cin >> Q;

    int input[n][3];

    for (int i = 0; i < n; i++)
    {
        cin >> input[i][0];
        cin >> input[i][1];
        cin >> input[i][2];
    }

    Grafo g(n * (Q + 1) + 2);

    for (int i = 0; i < n; i++)
    {

        for (int j = 0; i == 0 && j <= input[i][2]; j++)
        {
            int v = ((i)*Q + (j * input[i][0])) + 1;

            if (j * input[i][0] > Q)
                break;

            g.adicionaArco(0, v, j * input[i][1]);
        }

        for (int j = Q; i > 0 && j >= 0; j--)
        {
            int v = i * (Q + 1) + j + 1;

            // Veritice com aresta 0
            int u_0 = (i - 1) * (Q + 1) + j + 1;

            // cout << v << " " << u_0 << endl;

            g.adicionaArco(u_0, v, 0);

            int u_w[input[i][2]];
            for (int k = 1; k <= input[i][2]; k++)
            {
                u_w[k - 1] = -1;

                if (!(j - (k * input[i][0]) < 0))
                {
                    u_w[k - 1] = (i - 1) * (Q + 1) + (j - (k * input[i][0]) + 1);
                }
            }

            for (int k = 1; k <= input[i][2]; k++)
                if (!(u_w[k - 1] == -1))
                    g.adicionaArco(u_w[k - 1], v, (k * input[i][1]));
        }
    }

    cout << g;
    int *dist = g.caminhoMinimo(0, n * (Q + 1));
    for (int i = 0; i < n * (Q + 1); i++)
        cout << dist[i] << endl;
    // cout << "Distância mínima entre 0 e 24: " << dist[24] << endl;
    /*

    Grafo g(4);

    g.adicionaArco(0, 1, 2);
    g.adicionaArco(0, 2, 1);
    g.adicionaArco(1, 3, 3);
    g.adicionaArco(2, 3, 6);
    cout << "Grafo gerado:" << endl;
    cout << g;

    int *dist = g.caminhoMinimo(0, 3);
    cout << "Distância mínima entre 0 e 3: " << dist[3] << endl;
    free(dist);

    return 0;
    */
}
