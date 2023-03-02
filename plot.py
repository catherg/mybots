import constants as c
import matplotlib.pyplot as plt

x_arr = []
for i in range(0,101):
    x_arr.append(i)

first_arr = [0.01883965895408171, 0.01883965895408171, 0.01883965895408171, 3.5847823394005, 3.5847823394005, 3.5847823394005,
            3.5847823394005, 3.5903197618985923, 4.5828645033234965, 4.5828645033234965, 4.5828645033234965, 4.5828645033234965,
            4.5828645033234965, 4.5828645033234965, 4.5828645033234965, 4.5828645033234965, 4.5828645033234965, 4.5828645033234965,
            5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579,
            5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579,
            5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579, 5.246482004035579,
            5.246482004035579, 5.414275644663427, 5.414275644663427, 5.414275644663427, 5.450246877034866, 5.450246877034866,
            5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866,
            5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866,
            5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866,
            5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866,
            5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866,
            5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866, 5.450246877034866,
            6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055,
            6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055,
            6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055,
            6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055, 6.056155212107055]

second_arr = [1.9392616919280945, 1.9392616919280945, 1.9392616919280945, 2.308264129748808, 5.8692339189863, 5.8692339189863,
            5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863,
            5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863, 5.8692339189863,
            5.8692339189863, 5.8692339189863, 5.8692339189863, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364, 6.450198303082364,
            7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038,
            7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038,
            7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038, 7.702440114064038,
            7.702440114064038]
third_arr = [0.0027755671958527243, 0.0027755671958527243, 0.0027755671958527243, 0.0027755671958527243, 1.3879581337810087, 3.5281028539162698,
            3.5281028539162698, 3.5281028539162698, 3.5281028539162698, 3.5281028539162698, 3.817009118574163, 3.817009118574163,
            5.280513352827925, 5.280513352827925, 5.280513352827925, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899,
            6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899,
            6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899, 6.719918992384899,
            9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326,
            9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326,
            9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 9.774674906932326, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285,
            10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285, 10.80895742062285]

fourth_arr = [0.4142802787238552, 0.7162802784438552, 0.7162802784438552, 3.0250230959574296, 3.121488058774021, 5.337717685225546,
            5.337717685225546, 5.337717685225546, 5.337717685225546, 5.337717685225546, 5.438717885295842,5.438717885295842, 5.438717885295842,
            5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812,
            5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812,
            5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812,
            5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812, 5.938123485567812,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801,
            6.332123445327801, 6.332123445327801, 6.332123445327801, 6.332123445327801]

fifth_arr = [0.0542802787238552, 0.8421831677366374, 2.8421831677366374, 2.8421831677366374, 3.0414678073510224, 3.0414678073510224,
            3.732748420796416, 3.732748420796416, 3.732748420796416, 3.732748420796416, 3.732748420796416, 3.732748420796416, 3.923876381101438,
            3.923876381101438, 3.923876381101438, 3.923876381101438, 3.964104283896203, 3.964104283896203, 3.964104283896203, 3.964104283896203,
            4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812,
            4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812, 4.878123432567812,
            5.132483454512572, 5.132483454512572, 5.132483454512572, 5.132483454512572,  5.132483454512572, 5.132483454512572, 5.132483454512572,
            5.132483454512572, 5.132483454512572, 5.132483454512572, 5.132483454512572,  5.132483454512572, 5.132483454512572, 5.132483454512572,
            5.132483454512572, 5.132483454512572, 5.132483454512572, 5.132483454512572,  5.132483454512572, 5.132483454512572, 5.132483454512572,
            5.132483454512572, 5.132483454512572, 5.132483454512572, 5.132483454512572,  5.132483454512572, 5.132483454512572, 5.132483454512572,
            5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550,
            5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550,
            5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550,
            5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550,
            5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550, 5.568421102312550,
            5.589712109417689, 5.589712109417689, 5.589712109417689, 5.589712109417689]


plt.plot(x_arr, first_arr, label = "creature 1")
plt.plot(x_arr, fifth_arr, label = "creature 2")
plt.plot(x_arr, second_arr, label = "creature 3")
plt.plot(x_arr, fourth_arr, label = "creature 4")
plt.plot(x_arr, third_arr, label = "creature 5")
plt.xlabel("Number of Generations")
plt.ylabel("Fitness Value")
plt.legend()

plt.show()