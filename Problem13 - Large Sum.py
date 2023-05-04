data = "3710728753390210279879799822083759024651013574025046376937677490009712648124896970078050417018260538\
7432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250\
2306758820753934617117198031042104751377806324667689261670696623633820136378418383684178734361726757\
2811287981284997940806548193159262169127588983273844274228917432520321923589422876796487670272189318\
4745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951\
6217645714185656062950215722319658675507932419333164906352462741904929101432445813822663347944758178\
9257586771833721766196375159057923972824559883840758203565325359399008402633568948830189458628227828\
8018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586\
8651550600629586486153207527337195919142051725582971693888707715466499115593487603532921714970056938\
5437007057682668462462149565007647178729443837760453282654108756828443191190634694037855217779295145\
3612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045\
1742370690585186066044820762120981328786073396941281142660418086830619328460811191061556940512689692\
5193432545172838864191804704929321505864256304948362467221648435076201727918039944693004732956340691\
1573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126\
1833638482533015468619612434876768129753437594651580386287592878490201521685554828717201219257766954\
7818283375799310361474035685644909552709786479758116726320100436897842553539920931837441497806860984\
4840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332\
5995940689575653678210707492696653767632623544721069793950679652694742597709739166693763042633987085\
4105268470829908521139942736573411618276031500127165378607361501080857009149939512557028198746004375\
3582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275\
8890280257173322961917666871381993181104877019027125267680276078003013678680992525463401061632866526\
3627021854049770558562994658063623799314074625596224074486908231174977792365466257246923322810917141\
9143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470\
2305308117281643048762379196984248725503663878458311487696932154902810424020138335124462181441773470\
6378329949063625966649858761822122522551248676453367720186971698544312419572409913959008952310058822\
9554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236\
3777424253541129168427686553892620502491032657296723701913275725675285653248258265463092207058596522\
2979886027225833191312637514734199488953476574550118495701454879288984856827726077713721403798879715\
3829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539\
4095795306640523263253804410005965493915987959363529746152185502371307642255121183693803580388584903\
4169811622207297718615823667842468915799353296192262467957194401269043877107275048102390895523597457\
2318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672\
1130673970830472448381653387350234084564705807730882959174767140363198008187129011875491310547126581\
9762333104481838626951545633492636657289756340050042846280183517070527831839425882145521227251250327\
5512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886\
7550616496518477518073816883786109152735792970133762177842752192623401942399639168044983993173312731\
3292418570714734956691667468763466091503591467750499518671430235219628894890102423325116913619626622\
7326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818\
9714261791034259864720451689398942217982608807685287783646182799346313767754307809363333018982642090\
1084880252167467088321512018588354322381287695278671329612474782464538636993009049310363619763878039\
6218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411\
6066182629368283676474477923918033511098906979071485786944089552990653640447425576083659976645795096\
6602439640990538960712019821997604759949019723029764913982680032973156037120041377903785566085089252\
1673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791\
7863916702118749243199570064191796977759902830069915368713711936614952811305876380278410754449733078\
4078992311553556256114232242325503368544248891735344889911501440648020369068063960672322193204149535\
4150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280\
8261657077394832759223284594170652509451232523060822918802058777319719839450180888072429661980811197\
7715854250201654509041324580978688277894872185961772107838435069186155435662884062257473692284509516\
2084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690"

sum = 0
n = 0
while n < 5000:
    sum += int(data[n:n+50])
    n += 50
sum = str(sum)
print(sum[0:10])