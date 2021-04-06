import time
import draw_scene as scene
import Generator as gen
import NeuralNet as net
dims = (50,50)
n_layers = [3,8,1]
def one_shot(name):
    global dims,n_layers
    r_net = net.FFNN(n_layers)
    g_net = net.FFNN(n_layers)
    b_net = net.FFNN(n_layers)

    
    r_build = gen.Generator(dims,r_net)
    g_build = gen.Generator(dims,g_net)
    b_build = gen.Generator(dims,b_net)
    
    colours = [r_build,g_build,b_build]
    mapping = []
    for x in colours:
        x.genEnv(0)
        mapping.append(x.getEnv())
        
    main = scene.Draw(dims,mapping)
    main.save_image(f"Images//PerlinNoise{name}","PNG",main.res)


if __name__ == "__main__":
    pop = 100
    for x in range(pop):
        one_shot(str(x))
        print(f'Generated {x/pop * 100}%')
    print("running")
