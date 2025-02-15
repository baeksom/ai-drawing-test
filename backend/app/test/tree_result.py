class BaseResult:
    def __init__(self, index, title, result, score, summary=''):
        self.index = index
        self.title = title
        self.result = result
        self.score = score
        self.summary = summary
    

# tree type
TREE_TYPE_PINE = BaseResult(0, 
                            "소나무,삼목,상록수",
                            "- 소나무, 상록수와 비슷한 나무를 그린 당신은 본인을 활력이 넘치는 존재로 여깁니다. 강한 달성 욕구를 가지고 있으며 본인을 통제하고 질서 있는 행동을 추구합니다.",
                            [0, 0, 0, 0, 0])
TREE_TYPE_BUD = BaseResult(1,
                           "버드나무와 같이 밑으로 처지는 나무",
                           "- 버드나무처럼 밑으로 처지는 나무를 그린 사람은 내향적이며 폐쇄적인 경향을 가집니다. \n \
                            - 다른 사람의 영향을 받기 쉽고 활발하지 못하며 피로감을 쉽게 느낍니다.\n \
                            - 우울함을 가진 사람에게서 많이 보이는 특성입니다.\n \
                            - 가지가 아래로 처진 버드나무는 현실 세상으로 뻗어 나가는 것을 두려워하고, 과거에 대한 미련과 집착을 버리지 못하는 성향을 보일 수 있습니다.\n \
                            - 만일 오른쪽으로 가지가 쏠린 버드나무 그림을 그렸다면 매우 큰 두려움에 휩싸여 있거나 현실보단 공상을 즐길 가능성이 많습니다. 다른 의미로는, 예술적인 기질이 있는 사람이라고도 할 수 있습니다.\n \
                            ( 실수를 하지 않는 사람은 없습니다. ‘실패는 성공의 어머니‘라는 말이 있습니다. 전에 저지른 실수에 대해서 더 이상 후회의 생각을 않도록 노력하고 이 실수는 더 나은 나를 만들어주는 기회라는 생각과 함께 새로운 발걸음을 내딛는 당신이 되기를 기원합니다.)",
                            [0, 0, 1, 1, 0])
TREE_TYPE_DEAD = BaseResult(2,
                            "고목",
                            "- 당신이 고목을 그렸다면, 심각한 심리적 문제를 가지고 있을 수 있습니다. 내면에 열등감, 무력감, 우울함, 죄책감 같은 감정을 가지고 있지 않나요? 그렇다면 공허함과 좌절감이 가득하고, 의욕이 모두 상실된 상태로 보입니다.\n \
                            ( 대한민국 축구선수 ‘박지성’ 선수는 초등학생 시절, 덩치가 작아 ‘미키 마우스’라 불렸습니다. 또래 선수들에 비해 체구가 작고 연약했기 때문입니다. 박지성 선수는 이러한 신체적 조건을 컴플렉스로 여겼고 다른 사람들에게 열등감을 느꼈습니다. 그렇지만 박지성 선수는 감정에 굴복하지 않았고, 최고의 대한민국 축구선수가 되었습니다. 우울함과 열등감을 극복하기 위해서 중요한 것은 마음가짐입니다. )",
                            [0, 1, 1, 0, 1])
TREE_TYPE_STUB = BaseResult(3,
                            "그루터기",
                            "- 그루터기를 그린 당신은 자신의 힘으로는 감당할 수 없는 심적 외상이 있음을 나타냅니다. 만약 당신이 그린 그루터기에 새싹이 있다면, 당신의 무의식중에 이미 새 출발을 시작했다는 것입니다.\n \
                            ( 자신이 받은 상처를 원활하게 해소하기 위해서 심리 치료 기법 중 상대방과 대화를 통해 해결할 수 있는 ‘I Message’ 대화법과 유년 시기 받은 상처를 치료할 수 있는 ‘이마고 테라피’ 심리 치료를 추천합니다.\n \
                            *I Message 대화법이란 타인과 의사소통을 할 때 ‘나’를 주어로 하는 대화법입니다.\n \
                            예를 들어 “네가 무언가를 했을 때 나는 이런 감정을 느꼈어”라고 대화의 초점을 상대방에게 맞추지 않고 나의 마음이나 생각을 말하는 방식입니다. 상대방의 말이나 어떤 행위를 비난하지 않으면서 자신의 솔직한 생각과 감정 상태를 전달할 수 있는 장점이 있습니다.)",
                            [0, 0, 1, 1, 0])
TREE_TYPE_KEY = BaseResult(4,
                           "열쇠구멍 모양으로 그린 경우", "당신이 그린 그림은 뿌리가 고정되지 않아 불안정하고 기둥이 아래에서 위로 가는 동안 변함없이 굵기가 똑같으며 가지가 없습니다. 이러한 형태의 그림은 막연하고 공허한 느낌을 줍니다. 잎사귀를 표현하지 않고 마치 숟가락 모양처럼 동그란 형태의 나무는 정신적으로 불안하고 별다른 목표가 없는 상태를 나타냅니다. 즉, 바닥에 가라앉지 못하고 붕 떠있는 심리상태에 있음을 의미합니다.",
                           [0, 1, 0, 0, 0])

TREE_TYPE_RESULT = [TREE_TYPE_PINE, TREE_TYPE_BUD, TREE_TYPE_DEAD, TREE_TYPE_STUB, TREE_TYPE_KEY]

# tree root
TREE_ROOT_XRAY = BaseResult(0,
                            "엑스레이 사진처럼 지면을 그리고 뿌리를 적나라하게 보이게 그리는 것",
                            "- 땅속에 묻혀서 보이지 않아야 할 뿌리가 엑스레이를 찍은 듯이 보인다면 심리적인 문제가 있을 가능성이 있을 수 있으며, 현실을 검증하는 능력에 문제가 있을 수 있습니다. 이상과 현실을 구분하지 못한 경우 이런 그림을 그리기도 합니다.",
                            [0, 1, 0, 0, 0])
TREE_ROOT_HIGHLIGHT = BaseResult(1,
                                 "뿌리 강조",
                                 "- 나무뿌리를 강조해서 그린 사람은 미성숙하고 과거에 집착하는 경향을 보입니다. 현실에 적응하지 못하고, 미디어, 게임 등 자기만의 세계에 빠져 있을 가능성이 있습니다. 또한, 가족 속에서 안정을 느끼기를 원합니다.",
                                 [1, 1, 0, 1, 0])
TREE_ROOT_ABOVE = BaseResult(2,
                             "지면 위로 뿌리",
                             "- 뿌리가 지면 위로 올라와 있는 그림은 유년 시절 겪었던 상처와 트라우마를 잊지 못하고 현재까지 영향을 받고 있는 것으로 해석할 수 있습니다. 미성숙하거나 불안정했던 과거에 대한 관심을 나타냅니다. 만일 스스로에 대한 확신을 갖지 못하면, 자신을 탐구하기 위해 과거에 머무를 확률이 높습니다.",
                             [0, 1, 0, 0, 1])

TREE_ROOT_RESULT = [TREE_ROOT_XRAY, TREE_ROOT_ABOVE, TREE_ROOT_HIGHLIGHT]

# tree branch
TREE_BRANCH_NET = BaseResult(0,
                            "줄기에서 갈라진 가지가 점차적으로 세분되어 그물과 같은 모양",
                            "- 기둥에서 뻗어 나가는 가지는 사회적인 교류를 의미합니다. 가지가 복잡하고 많으면, 인간관계를 탁월하게 잘하는 사람일 가능성이 높습니다. 또한, 감수성이 풍부하고 외부로부터 자극에 잘 반응하는 사람일 가능성이 큽니다.\n \
                            - 가지가 지나치게 많은 경우는 인간관계가 복잡하고 정신적으로 산만하여 집중력이 부족하다고 해석됩니다.\n \
                            - 잎은 무성한데 잎을 받쳐주는 가지가 많지 않다면 욕심은 많고 현실은 무시하는 경향이 있습니다.",
                            [0, 0, 0, 0, 0],
                            "그물")
TREE_BRANCH_UP = BaseResult(1,
                            "가지가 옆쪽보다 위쪽을 뻗는 그림",
                            "- 당신은 주관이 뚜렷하고 활동적이며 열정적인 사람으로 보입니다. 하지만 사람에 관심이 없으며, 억제력이 부족하여 화를 잘 낼 수 있습니다.\n \
                            (당신의 능력과 의견은 조직에 큰 도움이 될 수 있습니다. 당신의 감정과 주관은 소중합니다.  당신이 다른 사람까지 챙길 수 있다면, 최고의 결과물을 낼 수 있을 것입니다.)",
                            [1, 0, 0, 1, 0],
                            "윗쪽으로 뻗는")
TREE_BRANCH_UNCLOSED = BaseResult(2,
                            "끝이 닫히지 않은 가지",
                            "- 개방적이며 관심사가 많아 여러 가지(취미, 공부, 주제 등)에 흥미를 가지고 있습니다. 당신은 다양한 시도에 두려움을 가지지 않는 자신감을 가진 사람입니다. 반면, 지나친 에너지에 자신의 충동을 적절히 통제하지 못할 수도 있습니다. ",
                            [0, 0, 1, 1, 1],
                            "끝이 닫히지 않은 가지")

TREE_BRANCH_RESULT = [TREE_BRANCH_NET, TREE_BRANCH_UP, TREE_BRANCH_UNCLOSED]

# tree leaf, fruit
TREE_LEAF_BIG = BaseResult(0,
                           "가지에 비하여 지나치게 큰 잎을 그리는 것",
                           "- 당신은 생활 속 스트레스로 인해 무력감을 가지고 있지만, 적응해 가고 있는 사람일 것입니다. 하지만 자기 부적절감을 과하게 극복하려는 경향을 나타내기도 합니다.\n \
                           * 자기 부적절감이란 본인 스스로 생각하기에 본인이 부족하다고 느끼고, 다른 사람에게 부정적인 평가를 받을 것이라고 걱정합니다.",
                           [0, 0, 1, 1, 1],
                           "잎이 큰")
TREE_LEAF_LEAFY = BaseResult(1,
                            "잎을 무성하게 그린 경우",
                            "- 당신은 생산성과 유능함을 중요시 생각하는 사람입니다.",
                            [1, 0, 0, 0, 0],
                            "잎무성한")
TREE_LEAF_FLOWER = BaseResult(2,
                              "꽃을 그리는 경우", 
                              "- 당신은 풍부한 감수성을 가진 사람입니다. 동시에 체면을 중시하기에 외적인 모습에 신경을 많이 쓰는 사람일 가능성이 높습니다. 때로는 자기 자신이 지나치게 뛰어나다고 생각하는 나르시시스트적인 경향을 보이기도 합니다.",
                              [1, 1, 0, 0, 0],
                              "꽃있음")
TREE_LEAF_FRUIT = BaseResult(3,
                            "열매가 있는 나무", 
                            "- 열매는 인정받고 싶은 욕구를 나타냅니다. 많은 열매는 일의 성과나 자신의 모든 면에 대해 의욕 또는 욕심을 가지고 있음을 나타냅니다. 이러한 욕심은 당신을 힘들게 만들 수도 있습니다.\n \
                            - 만일 열매가 많은 것과 대조되게 가지의 수가 적거나 기둥이 약하다면, 욕심은 많지만 현실적으로 접근이 쉽지 않은 공상에 가까운 목표를 세우고 있을 수 있습니다. 당장은 계획이나 과정이 풍성해 보일지 몰라도 얼마 지나지 않아서 지칠 수 있으니, 목표에 대한 세부적인 계획을 세워 하나씩 시작해 보는 것이 어떨까요?",
                            [1, 1, 0, 0, 0],
                            "열매있음")

TREE_LEAF_RESULT = [TREE_LEAF_BIG, TREE_LEAF_LEAFY, TREE_LEAF_FLOWER, TREE_LEAF_FRUIT]

# tree stem
TREE_STEM_RING = BaseResult(0, 
                            "나이테/나무껍질, 옹이가 있는 나무", 
                            "- 나이테, 나무껍질, 옹이는 유년 시절 어려움을 경험하고 상처를 받은 적이 있는 흔적입니다. 그러나 자주 마주친 나무의 특징일 수 있으므로 모든 사람에게 적용되는 해석은 아닙니다.",
                            [1, 1, 1, 1, 0],
                            "나이테_나무껍질_옹이_O")
TREE_STEM_ANIMAL = BaseResult(1, 
                              "작은 동물이나 곤충이 사는 나무",
                              "- 주변 환경에 대한 불안함으로 인한 보호받고 싶은 마음이 곤충이나 동물을 통해 드러난 것이라 할 수 있습니다.",
                              [0, 1, 1, 0, 1],
                              "동물_곤충_O")
TREE_STEM_RESULT = [TREE_STEM_RING, TREE_STEM_ANIMAL]

# tree size, location
TREE_SIZE_SMALL = BaseResult(0,
                             "그림을 작게 그렸을 경우",
                             "- 상대적으로 작은 그림을 그린 당신은 소속된 환경에서 적응에 어려움을 겪고 있다고 느끼고 있습니다. 당신은 자신이 속한 조직 내에서 자신을 자그마한 존재라고 생각하고 있습니다. 추가적으로 열등감, 무능력함, 불안정감 혹은 소심함, 수줍음을 나타냅니다. 즉, 자아 강도가 낮을 수 있음을 의미합니다.\n \
                            (모든 사람은 완벽하지 않으며 부족한 점이 있습니다. 누군가는 소심하고 수줍음이 많고, 또 다른 누군가는 지나치게 적극적일 수 있습니다. 그럼에도 불구하고 모든 사람들은 단점을 가짐과 동시에 자신을 빛나게 할 무기가 있을 것입니다.)",
                            [0, 0, 1, 1, 1])
TREE_LOCATION_LEFT = BaseResult(1, 
                                "왼쪽으로 치우친 그림",
                                "- 상대적으로 왼쪽으로 치우친 그림은 자의식이 강하고 내향적인 성향을 나타냅니다. 또한 과거로 퇴행하고자 하며, 공상적인 경향이 있습니다.\n \
                                (만약 위의 해석이 본인과 같다고 생각한다면, 자신의 능력을 믿고 자신감을 가지고 주어진 일과를 용기를 가지고 해결해 나가는 건 어떨까요? 자신에게 주어진 더 나은 미래를 향해 힘차게 나아가보세요!)",
                                [0, 0, 0, 1, 0])
TREE_LOCATION_MIDDLE = BaseResult(2, 
                                  "중앙에 그림",
                                  "- 중앙에 위치한 그림은 통상적으로 안정된 사람임을 나타냅니다.\n \
                                  - 단, 그림이 과하게 종이의 정중앙에 있을 경우는 완고한 성격을 나타냅니다. 이는 특히 인간관계에서 두드러지는 특성입니다.",
                                  [0, 0, 0, 0, 0])
TREE_LOCATION_RIGHT = BaseResult(3,
                                 "오른쪽으로 치우친 그림",
                                 "- 상대적으로 오른쪽으로 치우친 그림은 스스로가 안정된 사람임을 나타냅니다. 욕구 및 행동 통제가 잘 되는 사람일 가능성이 높습니다.",
                                 [1, 1, 0, 0, 0])
TREE_STEM_SMALL = BaseResult(4,
                             "작은 나무줄기", 
                             "- 상당히 작은 나무줄기는 현실에 대한 무력감, 부적응감을 갖고 있음을 나타냅니다.",
                             [0, 0, 1, 1, 1])

TREE_SIZE_RESULT = [TREE_SIZE_SMALL, TREE_LOCATION_LEFT, TREE_LOCATION_MIDDLE, TREE_LOCATION_RIGHT, TREE_STEM_SMALL]
