[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SyL_Oenm)
| Date              |          |
|:------------------|:---------|
| 15 November 2023 | Assigned |
| 21 November 2023 | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

**Improvement for this assignment is due by or on December 1. Improvements for all previous assignments need to be completed before November 27th.**

# KEEPING UP WITH CURRENT EVENTS, POLITICIAN PROPOSES POWER PRODUCTION FOR PLAUDITS

**Reported by `Official Mayor-Endorsed News`**

If you thought surveillance was a shocking trick, the Mayor's Office is all charged up about a new effort: sidelining the environment to feed the new manufacturing craze in `term-world`. As the Mayor commented during a recent presss conference, she's apparently "not the only one who's power hungry around here."

Until now, citizens haven't taken advantage of the digital riches in coal, oil, and, well renewables like solar and wind power (we guess, if you're into that) and the energizing effect they could have on the `term-world` economy. Forget about nature versus nuture, the new calling card is _nature versus neutrons_.

Each neighborhood is being asked to work together to provide a model for what electrification looks like in the world. What path will provide the charge for the future? Giga-what neighborhood will emerge as new luminaries? How will we continue to power hearth and ohm?

## Learning Outcomes

In this assignment you will:

* discover how to import custom modules and use them as `object`s
* continue to create `class`es and `object`s to achieve purpose-built tasks
* observe strange, but productive, `object` behaviors
* begin to explore the concept of `object` `inheritance`, a way to "template" mulitple objects at once

You will also continue to practice:

- Using data structures such as lists
- Writing class methods including constructors
- Writing Python code that uses loops
- Running Python programs
- Debugging Python programs
- Technical writing in Markdown
- Command line navigation
- Using version control (Git)

These assignment learning outcomes contribute to the following course learning outcomes described in the [course syllabus](https://github.com/cmpsc100-allegheny-college/course_information):

1. Apply Python programming principles to execute and explain computer code that implements interactive, novel solutions to a variety of computable problems.
2. Release code consistent with industry-standard practices using professional grade IDEs, command line tools, and version control tools.
3. Analyze and suggest revisions to existing Python language code to improve or add functionality.
4. Evaluate the practical and ethical implications of writing computer code and discuss the contexts, perceived effects, and impacts exerted on and by computer code as a cultural force or artifact.
5. Design, describe, and implement original projects incorporating standard practices and Python language principles.

## Completing `powerplant` content

For our final regular activity, we have some decisions to make: some about design and some about more-or-less environmentally-friendly options. This task is all about choices. 

Here is a list of broad goals, some of which we'll complete together:

* survey the array of fuel options and how to do use each
* charge a `.battery` file, logging how much each energy source generates
* design ways to generate power that leverage the strenghts of the sources to generate the most power
* pursue all of these goals to win a coveted prize for generating the most energy

### Energy sources

`term-world` boasts a mix of `Oil`, `Coal`, `Wind`, and `Solar` power options, available as part of the `resources` module.

|Type |Exhaustion |Energy yield |Amount yielded per request|
|:----|:----------|:------------|:--------------|
|`Oil`|Exhaustible|1667 kWh per barrel |5 barrels |
|`Coal`|Exhaustible|5549 kWh per short ton|7 short tons|
|`Solar`|Inexhaustible|1.2% panel wattage per second |1 second |
|`Wind`|Inexhaustible |Various, depending on `blade_size`†, wind speed |1 second |

`†` Maximum blade size is `115` meters; the larger the blade size, the slower the speed

#### Properties and methods of each source (by category)

##### Exhaustibles

Each exhaustible should use:

* an `energy` _property_ to store energy generated
* a `use` method to access the energy in the resource tapped

##### Inexhaustibles

###### `WindFarm`

* a `blade_size` property to set the size of the turbine blade
* a `super().__init__()` call to access properties and methods of the `Wind`

###### `SolarField`

* a `wattage` property to set the maximum wattage of the solar panel
* a `super().__init__()` call to access properties and methods of `Solar` energy

#### Note about `Exhaustibility`

##### Exhaustibles

Anything marked `Exhaustible` has a finite limit. At some point, the world runs out. It could happen now, it could happen in a year (or century). We simply don't know.

##### Inexhaustibles

While true that these sources do not have a limit, they can only be "harvested" during the right conditions (i.e. a wind greater than `5` mph or on sunny days that the sun is _actually_ showing). The `term-world` news page is a great source for this information. 

To call up the news page, use `CTRL + SHIFT + P` and type `menu` to filter the results. `term-world Menu: Show` should appear as an option.

### `reflection.md`

Don't forget to finish the `reflection.md` file in the `paperwork` folder!

## Improvement suggestions

**Improvement for this assignment is due by or on December 1. Improvements for all previous assignments need to be completed before November 27th.**

Here are some suggestions for improvements you can, **but are not limited to** use:

|Improvement Suggestions |Description        |
|:-----------------------|:------------------|
|Objects            |Create an object that uses stored power |
|Objects            |Create an object hooked up directly to a power source |
|Conditional statements |Create an interface to choose power sources to use |
|Iteration          |Automate power generation based on time, demand, or other reason |
|Data visualization           |Create a dashboard (using `rich`) to visualize the contents of the `.battery`|
|Data structures/Objects    |Display the weather conditions underlying the renewable sources†|
|Objects            |Find and use the secret power source† |
|Data visualization |Create a poster about the `term-world` Energy Development and Industrial Utility Management supply chain |

`†` _Probably_ uses the `dir()` function to begin to explore `object`s

**Make sure to link your issue with the pull request you used to make your actually improvement.**

**If you are not following an improvement suggestion you need to have your improvement suggestion checked by the professor before proceeding.**

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.