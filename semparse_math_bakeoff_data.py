from example import Example

mathbake_train = [
    Example(input="volms sniese kugns", semantics=None, denotation=4),
    Example(input="volms sklofg glarc", semantics=None, denotation=3),
    Example(input="fribbs sniese kugns", semantics=None, denotation=3),
    Example(input="scincs sniese volms", semantics=None, denotation=7),
    Example(input="fribbs sklofg glarc", semantics=None, denotation=2),
    Example(input="scincs sklofg fribbs", semantics=None, denotation=2),
    Example(input="scincs sklofg scincs", semantics=None, denotation=0),
    Example(input="glarc sklofg scincs", semantics=None, denotation=-4),
    Example(input="sherle sklofg fribbs", semantics=None, denotation=3),
    Example(input="fribbs sklofg sherle", semantics=None, denotation=-3),
    Example(input="fribbs sklofg scincs", semantics=None, denotation=-2),
    Example(input="glarc sklofg thouch glarc", semantics=None, denotation=0),
    Example(input="kugns sklofg thouch kugns", semantics=None, denotation=2),
    Example(input="volms sniese scwokt volms", semantics=None, denotation=6),
    Example(input="kugns sklofg scwokt kugns", semantics=None, denotation=0),
    Example(input="scwokt volms sniese kugns", semantics=None, denotation=4),
    Example(input="volms sklofg thouch sherle", semantics=None, denotation=8),
    Example(input="scwokt fribbs sklofg glarc", semantics=None, denotation=2),
    Example(input="kugns sklofg thouch sherle", semantics=None, denotation=6),
    Example(input="scwokt scincs sklofg kugns", semantics=None, denotation=3),
    Example(input="thouch kugns sniese sherle", semantics=None, denotation=4),
    Example(input="volms sniese scwokt fribbs", semantics=None, denotation=5),
    Example(input="fribbs sniese thouch kugns", semantics=None, denotation=1),
    Example(input="sherle sniese thouch glarc", semantics=None, denotation=5),
    Example(input="thouch volms sklofg kugns", semantics=None, denotation=-4),
    Example(input="scincs sniese thouch glarc", semantics=None, denotation=4),
    Example(input="thouch scincs sniese scincs", semantics=None, denotation=0),
    Example(input="glarc sniese thouch scincs", semantics=None, denotation=-4),
    Example(input="volms sklofg scwokt sherle", semantics=None, denotation=-2),
    Example(input="thouch fribbs sniese fribbs", semantics=None, denotation=0),
    Example(input="thouch sherle sklofg volms", semantics=None, denotation=-8),
    Example(input="scwokt fribbs sniese fribbs", semantics=None, denotation=4),
    Example(input="scwokt glarc sklofg sherle", semantics=None, denotation=-5),
    Example(input="thouch sherle sklofg kugns", semantics=None, denotation=-6),
    Example(input="scwokt volms sklofg sherle", semantics=None, denotation=-2),
    Example(input="sherle sniese scwokt scincs", semantics=None, denotation=9),
    Example(input="scincs sniese thouch sherle", semantics=None, denotation=-1),
    Example(input="scwokt scincs sklofg sherle", semantics=None, denotation=-1),
    Example(input="thouch sherle sniese fribbs", semantics=None, denotation=-3),
    Example(input="thouch scincs sklofg fribbs", semantics=None, denotation=-6),
    Example(input="scwokt volms sniese thouch kugns", semantics=None, denotation=2),
    Example(input="scwokt volms sklofg scwokt glarc", semantics=None, denotation=3),
    Example(input="scwokt thouch kugns sniese kugns", semantics=None, denotation=2),
    Example(input="thouch glarc sniese scwokt volms", semantics=None, denotation=3),
    Example(input="scwokt glarc sniese thouch glarc", semantics=None, denotation=0),
    Example(input="kugns sklofg scwokt thouch glarc", semantics=None, denotation=1),
    Example(input="scwokt thouch kugns sniese volms", semantics=None, denotation=4),
    Example(input="thouch kugns sklofg thouch kugns", semantics=None, denotation=0),
    Example(input="scwokt thouch volms sniese kugns", semantics=None, denotation=4),
    Example(input="scwokt thouch fribbs sniese kugns", semantics=None, denotation=3),
    Example(input="scwokt kugns sklofg scwokt volms", semantics=None, denotation=-2),
    Example(input="sherle sniese scwokt thouch volms", semantics=None, denotation=8),
    Example(input="thouch volms sniese scwokt kugns", semantics=None, denotation=-2),
    Example(input="scwokt scincs sniese scwokt volms", semantics=None, denotation=7),
    Example(input="thouch glarc sniese thouch kugns", semantics=None, denotation=-1),
    Example(input="thouch volms sniese thouch glarc", semantics=None, denotation=-3),
    Example(input="scwokt thouch fribbs sniese glarc", semantics=None, denotation=2),
    Example(input="fribbs sniese scwokt thouch glarc", semantics=None, denotation=2),
    Example(input="scwokt scincs sniese thouch kugns", semantics=None, denotation=3),
    Example(input="scwokt volms sklofg scwokt fribbs", semantics=None, denotation=1),
    Example(input="scwokt sherle sniese thouch volms", semantics=None, denotation=2),
    Example(input="scincs sklofg scwokt thouch volms", semantics=None, denotation=1),
    Example(input="thouch glarc sklofg thouch fribbs", semantics=None, denotation=2),
    Example(input="scwokt scincs sklofg scwokt kugns", semantics=None, denotation=3),
    Example(input="scwokt sherle sklofg thouch volms", semantics=None, denotation=8),
    Example(input="fribbs sniese scwokt thouch volms", semantics=None, denotation=5),
    Example(input="thouch fribbs sniese scwokt volms", semantics=None, denotation=1),
    Example(input="scwokt thouch volms sniese fribbs", semantics=None, denotation=5),
    Example(input="scincs sniese scwokt thouch glarc", semantics=None, denotation=4),
    Example(input="thouch kugns sniese scwokt sherle", semantics=None, denotation=4),
    Example(input="scwokt thouch scincs sniese kugns", semantics=None, denotation=5),
    Example(input="thouch glarc sklofg thouch scincs", semantics=None, denotation=4),
    Example(input="scwokt sherle sklofg thouch glarc", semantics=None, denotation=5),
    Example(input="fribbs sniese glarc sniese fribbs", semantics=None, denotation=4),
    Example(input="glarc sklofg scwokt thouch volms", semantics=None, denotation=-3),
    Example(input="thouch fribbs sklofg thouch fribbs", semantics=None, denotation=0),
    Example(input="thouch fribbs sniese scwokt kugns", semantics=None, denotation=-1),
    Example(input="scwokt thouch fribbs sklofg fribbs", semantics=None, denotation=0),
    Example(input="scwokt fribbs sklofg scwokt volms", semantics=None, denotation=-1),
    Example(input="thouch kugns sklofg scwokt scincs", semantics=None, denotation=-5),
    Example(input="thouch scincs sklofg thouch sherle", semantics=None, denotation=1),
    Example(input="thouch scincs sniese thouch kugns", semantics=None, denotation=-5),
    Example(input="thouch fribbs sklofg scwokt kugns", semantics=None, denotation=-3),
    Example(input="thouch sherle sklofg thouch volms", semantics=None, denotation=-2),
    Example(input="scwokt kugns sniese thouch fribbs", semantics=None, denotation=-1),
    Example(input="scwokt thouch kugns sklofg fribbs", semantics=None, denotation=-1),
    Example(input="thouch scincs sklofg thouch kugns", semantics=None, denotation=-3),
    Example(input="volms sklofg scwokt thouch sherle", semantics=None, denotation=-2),
    Example(input="thouch sherle sklofg scwokt glarc", semantics=None, denotation=-5),
    Example(input="scwokt thouch fribbs sklofg volms", semantics=None, denotation=-1),
    Example(input="thouch volms sklofg scwokt scincs", semantics=None, denotation=-7),
    Example(input="thouch fribbs sniese thouch volms", semantics=None, denotation=-5),
    Example(input="thouch fribbs sklofg scwokt volms", semantics=None, denotation=-5),
    Example(input="fribbs sklofg scwokt thouch fribbs", semantics=None, denotation=0),
    Example(input="scwokt glarc sklofg scwokt sherle", semantics=None, denotation=-5),
    Example(input="thouch fribbs sniese scwokt fribbs", semantics=None, denotation=0),
    Example(input="scwokt sherle sniese thouch sherle", semantics=None, denotation=0),
    Example(input="scwokt scincs sklofg thouch fribbs", semantics=None, denotation=6),
    Example(input="scwokt volms sklofg scwokt scincs", semantics=None, denotation=-1),
    Example(input="thouch sherle sklofg scwokt scincs", semantics=None, denotation=-9),
    Example(input="scwokt fribbs sniese thouch scincs", semantics=None, denotation=-2),
    Example(input="thouch fribbs sniese thouch scincs", semantics=None, denotation=-6),
    Example(input="thouch sherle sniese thouch fribbs", semantics=None, denotation=-7),
    Example(input="scwokt glarc sniese scwokt thouch volms", semantics=None, denotation=3),
    Example(input="thouch glarc sniese scwokt thouch kugns", semantics=None, denotation=1),
    Example(input="sherle sniese thouch scincs sklofg glarc", semantics=None, denotation=1),
    Example(input="scwokt sherle sklofg scwokt thouch volms", semantics=None, denotation=2),
    Example(input="scwokt thouch glarc sklofg thouch sherle", semantics=None, denotation=5),
    Example(input="scwokt thouch glarc sklofg scwokt kugns", semantics=None, denotation=-1),
    Example(input="scwokt thouch scincs sklofg thouch volms", semantics=None, denotation=7),
    Example(input="scwokt thouch scincs sniese thouch kugns", semantics=None, denotation=3),
    Example(input="scwokt thouch sherle sniese thouch volms", semantics=None, denotation=2),
    Example(input="thouch kugns sklofg scwokt thouch volms", semantics=None, denotation=-4),
    Example(input="sherle sklofg scincs sklofg scwokt glarc", semantics=None, denotation=1),
    Example(input="scwokt thouch glarc sniese thouch volms", semantics=None, denotation=-3),
    Example(input="scwokt thouch glarc sniese thouch kugns", semantics=None, denotation=-1),
    Example(input="scwokt thouch kugns sniese scwokt scincs", semantics=None, denotation=5),
    Example(input="scwokt thouch fribbs sklofg thouch kugns", semantics=None, denotation=3),
    Example(input="scwokt thouch scincs sniese scwokt kugns", semantics=None, denotation=5),
    Example(input="fribbs sklofg thouch volms sniese scincs", semantics=None, denotation=9),
    Example(input="thouch kugns sniese scwokt thouch glarc", semantics=None, denotation=-1),
    Example(input="thouch sherle sniese kugns sniese glarc", semantics=None, denotation=-4),
    Example(input="scwokt thouch glarc sniese scwokt sherle", semantics=None, denotation=5),
    Example(input="thouch kugns sklofg scwokt thouch glarc", semantics=None, denotation=-1),
    Example(input="thouch sherle sniese scwokt thouch volms", semantics=None, denotation=-2),
    Example(input="thouch volms sklofg scwokt thouch sherle", semantics=None, denotation=-8),
    Example(input="scwokt thouch kugns sniese thouch fribbs", semantics=None, denotation=-1),
    Example(input="scwokt thouch volms sklofg scwokt scincs", semantics=None, denotation=-1),
    Example(input="thouch glarc sklofg scwokt thouch scincs", semantics=None, denotation=-4),
    Example(input="scwokt fribbs sklofg scwokt thouch volms", semantics=None, denotation=-1),
    Example(input="scwokt sherle sklofg scwokt thouch sherle", semantics=None, denotation=0),
    Example(input="scwokt thouch kugns sklofg scwokt fribbs", semantics=None, denotation=-1),
    Example(input="scwokt volms sklofg scwokt thouch scincs", semantics=None, denotation=-1),
    Example(input="scincs sklofg thouch glarc sklofg sherle", semantics=None, denotation=-1),
    Example(input="thouch scincs sniese scwokt thouch glarc", semantics=None, denotation=-4),
    Example(input="scwokt thouch glarc sklofg scwokt sherle", semantics=None, denotation=-5),
    Example(input="scwokt fribbs sniese scwokt thouch fribbs", semantics=None, denotation=4),
    Example(input="scwokt thouch fribbs sniese thouch sherle", semantics=None, denotation=-3),
    Example(input="thouch fribbs sklofg scwokt thouch scincs", semantics=None, denotation=-6),
    Example(input="sherle sklofg thouch scincs sniese scincs", semantics=None, denotation=13),
    Example(input="scwokt thouch scincs sklofg scwokt sherle", semantics=None, denotation=-1),
    Example(input="scwokt thouch sherle sniese scwokt sherle", semantics=None, denotation=10),
    Example(input="scwokt thouch kugns sklofg scwokt thouch kugns", semantics=None, denotation=0),
    Example(input="scincs sniese scwokt thouch glarc sklofg volms", semantics=None, denotation=1),
    Example(input="thouch kugns sklofg volms sniese scwokt volms", semantics=None, denotation=-1),
    Example(input="scwokt scincs sklofg thouch kugns sniese kugns", semantics=None, denotation=6),
    Example(input="kugns sklofg thouch kugns sklofg thouch sherle", semantics=None, denotation=7),
    Example(input="scwokt thouch sherle sniese volms sniese kugns", semantics=None, denotation=9),
    Example(input="scwokt sherle sklofg fribbs sklofg thouch volms", semantics=None, denotation=6),
    Example(input="scwokt scincs sklofg scwokt volms sklofg volms", semantics=None, denotation=-2),
    Example(input="scwokt kugns sniese thouch kugns sklofg fribbs", semantics=None, denotation=-2),
    Example(input="thouch sherle sniese kugns sniese thouch sherle", semantics=None, denotation=-9),
    Example(input="sherle sklofg scwokt glarc sniese scwokt sherle", semantics=None, denotation=10),
    Example(input="scwokt kugns sniese fribbs sniese thouch scincs", semantics=None, denotation=-1),
    Example(input="scwokt thouch kugns sklofg scwokt thouch sherle", semantics=None, denotation=-4),
    Example(input="scwokt thouch scincs sniese scwokt thouch fribbs", semantics=None, denotation=6),
    Example(input="thouch sherle sniese scincs sniese thouch fribbs", semantics=None, denotation=-3),
    Example(input="scwokt thouch fribbs sklofg scwokt thouch sherle", semantics=None, denotation=-3),
    Example(input="thouch kugns sklofg scwokt kugns sklofg thouch volms", semantics=None, denotation=1),
    Example(input="scwokt volms sniese thouch kugns sniese thouch kugns", semantics=None, denotation=1),
    Example(input="scwokt glarc sniese scwokt glarc sklofg scwokt glarc", semantics=None, denotation=0),
    Example(input="thouch glarc sklofg scwokt thouch kugns sklofg glarc", semantics=None, denotation=-1),
    Example(input="scwokt thouch glarc sklofg glarc sklofg scwokt volms", semantics=None, denotation=-3),
    Example(input="volms sniese scwokt thouch sherle sniese thouch kugns", semantics=None, denotation=7),
    Example(input="scwokt kugns sklofg scwokt glarc sniese scwokt sherle", semantics=None, denotation=6),
    Example(input="scwokt volms sniese scwokt thouch glarc sniese fribbs", semantics=None, denotation=5),
    Example(input="kugns sniese scwokt fribbs sniese scwokt thouch sherle", semantics=None, denotation=8),
    Example(input="scwokt thouch sherle sklofg fribbs sklofg thouch volms", semantics=None, denotation=6),
    Example(input="scwokt thouch scincs sniese scwokt kugns sklofg fribbs", semantics=None, denotation=3),
    Example(input="thouch sherle sklofg thouch volms sniese scwokt scincs", semantics=None, denotation=2),
    Example(input="sherle sniese scwokt thouch scincs sniese scwokt glarc", semantics=None, denotation=9),
    Example(input="scwokt glarc sklofg thouch fribbs sklofg scwokt sherle", semantics=None, denotation=-3),
    Example(input="thouch kugns sklofg scwokt thouch scincs sklofg scincs", semantics=None, denotation=-9),
    Example(input="scincs sniese thouch glarc sklofg scwokt thouch sherle", semantics=None, denotation=-1),
    Example(input="thouch kugns sniese thouch scincs sklofg scwokt sherle", semantics=None, denotation=-10),
    Example(input="thouch sherle sklofg scwokt thouch scincs sniese fribbs", semantics=None, denotation=-7),
    Example(input="thouch scincs sniese scwokt thouch sherle sklofg fribbs", semantics=None, denotation=-1),
    Example(input="kugns sklofg scwokt thouch glarc sklofg scwokt thouch glarc", semantics=None, denotation=1),
    Example(input="scwokt glarc sniese scwokt scincs sniese scwokt thouch glarc", semantics=None, denotation=4),
    Example(input="scwokt thouch volms sniese scwokt kugns sklofg thouch sherle", semantics=None, denotation=9),
    Example(input="thouch volms sniese scwokt thouch glarc sklofg thouch kugns", semantics=None, denotation=-2),
    Example(input="scwokt fribbs sniese scwokt thouch volms sklofg thouch glarc", semantics=None, denotation=5),
    Example(input="thouch glarc sklofg scwokt thouch volms sklofg scwokt kugns", semantics=None, denotation=-4),
    Example(input="scincs sklofg scwokt thouch kugns sklofg scwokt thouch fribbs", semantics=None, denotation=1),
    Example(input="scwokt thouch scincs sklofg thouch sherle sniese thouch volms", semantics=None, denotation=6),
    Example(input="scwokt thouch scincs sniese scwokt sherle sklofg thouch glarc", semantics=None, denotation=9),
    Example(input="thouch sherle sniese scwokt thouch glarc sklofg thouch sherle", semantics=None, denotation=0),
    Example(input="scwokt thouch sherle sniese scincs sklofg scwokt thouch scincs", semantics=None, denotation=5),
    Example(input="thouch sherle sniese thouch scincs sklofg scwokt thouch kugns", semantics=None, denotation=-10),
    Example(input="scwokt fribbs sniese scwokt scincs sniese scwokt thouch scincs", semantics=None, denotation=10),
    Example(input="thouch sherle sniese scwokt thouch sherle sniese thouch sherle", semantics=None, denotation=-5),
    Example(input="thouch fribbs sniese scwokt thouch volms sklofg scwokt thouch glarc", semantics=None, denotation=1),
    Example(input="scwokt thouch fribbs sniese scwokt thouch scincs sklofg scwokt glarc", semantics=None, denotation=6),
    Example(input="scwokt kugns sklofg scwokt thouch sherle sniese scwokt thouch glarc", semantics=None, denotation=-4),
    Example(input="scwokt volms sklofg scwokt thouch fribbs sklofg scwokt thouch volms", semantics=None, denotation=-2),
    Example(input="scwokt kugns sklofg scwokt thouch kugns sklofg scwokt thouch sherle", semantics=None, denotation=-5),
    Example(input="scwokt thouch volms sklofg scwokt thouch kugns sklofg scwokt scincs", semantics=None, denotation=-2),
    Example(input="scwokt sherle sniese scwokt thouch fribbs sklofg scwokt thouch scincs", semantics=None, denotation=3),
    Example(input="scwokt fribbs sniese scwokt thouch fribbs sklofg scwokt thouch scincs", semantics=None, denotation=0),
    Example(input="scwokt thouch fribbs sklofg scwokt volms sklofg scwokt thouch fribbs", semantics=None, denotation=-3)
]

mathbake_dev = [
    Example(input="sherle sklofg glarc", semantics=None, denotation=5),
    Example(input="kugns sklofg scwokt glarc", semantics=None, denotation=1),
    Example(input="thouch volms sniese volms", semantics=None, denotation=0),
    Example(input="kugns sniese scwokt kugns", semantics=None, denotation=2),
    Example(input="fribbs sniese scwokt kugns", semantics=None, denotation=3),
    Example(input="scwokt fribbs sniese kugns", semantics=None, denotation=3),
    Example(input="thouch volms sklofg glarc", semantics=None, denotation=-3),
    Example(input="scwokt kugns sklofg sherle", semantics=None, denotation=-4),
    Example(input="thouch sherle sniese sherle", semantics=None, denotation=0),
    Example(input="scwokt fribbs sklofg sherle", semantics=None, denotation=-3),
    Example(input="thouch kugns sniese scwokt volms", semantics=None, denotation=2),
    Example(input="scwokt sherle sklofg scwokt glarc", semantics=None, denotation=5),
    Example(input="scincs sniese scwokt thouch volms", semantics=None, denotation=7),
    Example(input="scwokt thouch fribbs sniese volms", semantics=None, denotation=5),
    Example(input="scwokt fribbs sklofg thouch volms", semantics=None, denotation=5),
    Example(input="scwokt fribbs sniese thouch volms", semantics=None, denotation=-1),
    Example(input="scincs sniese scwokt thouch fribbs", semantics=None, denotation=6),
    Example(input="thouch sherle sklofg scwokt kugns", semantics=None, denotation=-6),
    Example(input="scwokt scincs sklofg thouch scincs", semantics=None, denotation=8),
    Example(input="thouch scincs sklofg thouch glarc", semantics=None, denotation=-4),
    Example(input="scwokt scincs sklofg scwokt sherle", semantics=None, denotation=-1),
    Example(input="thouch scincs sklofg scwokt scincs", semantics=None, denotation=-8),
    Example(input="scwokt fribbs sniese thouch sherle", semantics=None, denotation=-3),
    Example(input="thouch sherle sklofg scwokt fribbs", semantics=None, denotation=-7),
    Example(input="glarc sklofg scwokt kugns sklofg volms", semantics=None, denotation=-4),
    Example(input="scwokt thouch sherle sklofg scwokt glarc", semantics=None, denotation=5),
    Example(input="scwokt thouch sherle sniese scwokt kugns", semantics=None, denotation=6),
    Example(input="scwokt thouch fribbs sniese thouch kugns", semantics=None, denotation=1),
    Example(input="thouch glarc sklofg scwokt thouch kugns", semantics=None, denotation=-1),
    Example(input="thouch fribbs sklofg scwokt thouch kugns", semantics=None, denotation=-3),
    Example(input="scwokt scincs sklofg scwokt thouch fribbs", semantics=None, denotation=2),
    Example(input="scwokt thouch glarc sklofg scwokt scincs", semantics=None, denotation=-4),
    Example(input="scwokt thouch scincs sniese scwokt scincs", semantics=None, denotation=8),
    Example(input="glarc sklofg glarc sniese scwokt thouch volms", semantics=None, denotation=3),
    Example(input="scwokt thouch volms sklofg scwokt thouch volms", semantics=None, denotation=0),
    Example(input="scwokt kugns sniese fribbs sniese thouch volms", semantics=None, denotation=0),
    Example(input="scwokt sherle sklofg thouch glarc sklofg glarc", semantics=None, denotation=5),
    Example(input="thouch volms sniese thouch glarc sklofg sherle", semantics=None, denotation=-8),
    Example(input="scwokt thouch scincs sklofg scwokt thouch kugns", semantics=None, denotation=3),
    Example(input="scwokt thouch volms sniese scwokt thouch fribbs", semantics=None, denotation=5),
    Example(input="fribbs sklofg scwokt thouch volms sniese fribbs", semantics=None, denotation=1),
    Example(input="thouch sherle sniese scwokt kugns sniese thouch kugns", semantics=None, denotation=-5),
    Example(input="scwokt thouch glarc sklofg thouch glarc sklofg scincs", semantics=None, denotation=-4),
    Example(input="scwokt sherle sklofg scwokt scincs sklofg scwokt volms", semantics=None, denotation=-2),
    Example(input="scwokt fribbs sklofg scwokt thouch sherle sklofg scincs", semantics=None, denotation=-7),
    Example(input="scwokt thouch sherle sklofg scwokt volms sklofg thouch scincs", semantics=None, denotation=6),
    Example(input="scwokt thouch glarc sklofg volms sklofg scwokt thouch scincs", semantics=None, denotation=-7),
    Example(input="thouch glarc sniese scwokt fribbs sniese scwokt thouch sherle", semantics=None, denotation=7),
    Example(input="scwokt thouch sherle sklofg scwokt scincs sniese scwokt thouch volms", semantics=None, denotation=4),
    Example(input="thouch scincs sniese scwokt thouch scincs sklofg scwokt thouch volms", semantics=None, denotation=-3)
]

