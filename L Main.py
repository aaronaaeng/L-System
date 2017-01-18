import DrawSystem
import LSystem
import Rule


def main():
    rule_set = [Rule.Rule("X", " F-[[X]+X]+F[+FX]-X"), Rule.Rule("F", "FF")]
    lin_system = LSystem.LSystem("X", rule_set)

    draw(lin_system)


def draw(l_system):
    for i in range(0, 6):
        l_system.generate()
    drawer = DrawSystem.DrawSystem(l_system.get_sentence(), 5, 25)
    drawer.render()

if __name__ == "__main__":
    main()
