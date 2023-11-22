import random

random_team_names = [
    'The Brainy Bunch',
    'Trivia Titans',
    'Smarty Pants',
    'The Wise Owls',
    'The Quiz Wizards',
    'The Think Tank',
    'The Know-It-Alls',
    'The Quizmasters',
    'The Smart Cookies',
    'The Brainiacs',
    'The Quiz Whizzes',
    'The Knowledge Kings',
    'The Intellectuals',
    'The Trivia Geniuses',
    'The Fact Fanatics',
    'The Information Gurus',
    'The Logic Legends',
    'The Wisdom Warriors',
    'The Data Doyens',
    'The Insightful Inquisitors',
    'The Rational Rulers',
    'The IQ Innovators',
    'The Sharp Scholars',
    'The Puzzled Professors',
    'The Curious Connoisseurs',
    'The Mental Mavericks',
    'The Wisdom Seekers',
    'The Curious Minds',
    'The Analytical Aces',
    'The Perceptive Pioneers',
    'The Savvy Sages',
    'The Clever Cognoscenti',
    'The Witty Whiz Kids',
    'The Sharpshooters',
    'The Clever Foxes',
    'The Quick Thinkers',
    'The Creative Cerebrums',
    'The Smart Alecks',
    'The Savvy Scholars',
    'The Intuitive Investigators',
    'The Problem Solvers',
    'The Sharp Schemers',
    'The Astute Detectives',
    'The Mindful Mediators',
    'The Insightful Interpreters',
    'The Thoughtful Theorists',
    'The Logical Leaders',
    'The Knowledge Knights',
    'The Intellectual Innovators',
    'The Analytical Architects',
    'The Data Defenders',
    'The Pragmatic Puzzlers',
    'The Wise Wits',
    'The Cerebral Seekers',
    'The Quick Studies',
    'The Calculated Connoisseurs',
    'The Bright Brains',
    'The Keen Observers',
    'The Shrewd Strategists',
    'The Sharp Scholars',
    'The Problem-Solving Pioneers',
    'The Bright Sparks',
    'The Astute Analysts',
    'The Perceptive Prodigies',
    'The Savvy Sleuths',
    'The Ingenious Investigators',
    'The Sharp Sleuths',
    'The Shrewd Schemers',
    'The Creative Controllers',
    'The Quick Quizzers',
    'The Brainstorming Bees',
    'The Clever Critics',
    'The Intuitive Investigators',
    'The Analytical Achievers',
    'The Knowledge Keepers',
    'The Intellectual Icons',
    'The Problem-Solving Pundits',
    'The Wise Workers',
    'The Thoughtful Thinkers',
    'The Logical Luminaries',
    'The Rational Rascals',
    'The Analytical Artists',
    'Flaming Ball Bros',
    'The Clever Comrades',
    'The Sharp Specialists',
    'The Quick Questioners',
    'The Curious Creatures',
    'The Clever Coordinators',
    'The Intrepid Inquirers',
    'The Knowledgeable Navigators',
    'The Intellectual Instructors',
    'The Problem-Solving Pilots',
    'The Wise Wayfarers',
    'The Thoughtful Tacticians',
    'The Logical Learners',
    'The Rational Researchers',
    'The Analytical Adventurers',
    'The Clever Captains',
    'The Quick Queriers',
    'The Curious Commanders',
    'The Sharp Sages',
    'The Intrepid Investigators',
    'The Knowledgeable Knights',
    'The Intellectual Explorers',
    'The Problem-Solving Prodigies',
    'The Wise Wanderers',
    'The Thoughtful Trailblazers',
    'The Logical Leaders',
    'The Rational Revolutionaries',
    'The Quizonauts',
    'The Sage Squad',
    'The Enigma Ensemble',
    'The Witty Wizards',
    'The Puzzled Prodigies',
    'The Brainy Battalion',
    'The Knowledge Krew',
    'The Think Tank Tribe',
    'The Trivia Trailblazers',
    'The Wise Whiz Kids',
    'The Clever Crusaders',
    'The Logic Luminaries',
    'The Insightful Investigators',
    'The Data Dynamo',
    'The Mindful Masters',
    'The Curious Cartographers',
    'The Analytical Architects',
    'The Perceptive Pathfinders',
    'The Savvy Scholars',
    'The Clever Conquerors',
    'The Quick Questers',
    'The Creative Connoisseurs',
    'The Smart Seekers',
    'The Astute Adventurers',
    'The Sharp Strategists',
    'The Problem-Solving Pioneers',
    'The Bright Brains',
    'The Keen Observers',
    'The Shrewd Strategists',
    'The Sharp Scholars',
    'The Problem-Solving Pioneers',
    'The Bright Sparks',
    'The Astute Analysts',
    'The Perceptive Prodigies',
    'The Savvy Sleuths',
    'The Ingenious Investigators',
    'The Sharp Sleuths',
    'The Shrewd Schemers',
    'The Creative Controllers',
    'The Quick Quizzers',
    'The Brainstorming Bees',
    'The Clever Critics',
    'The Intuitive Investigators',
    'The Analytical Achievers',
    'The Knowledge Keepers',
    'The Intellectual Icons',
    'The Problem-Solving Pundits',
    'The Wise Workers',
    'The Thoughtful Thinkers',
    'The Logical Luminaries',
    'The Rational Rascals',
    'The Analytical Artists',
    'The Clever Comrades',
    'The Sharp Specialists',
    'The Quick Questioners',
    'The Curious Creatures',
    'The Clever Coordinators',
    'The Intrepid Inquirers',
    'The Knowledgeable Navigators',
    'The Intellectual Instructors',
    'The Problem-Solving Pilots',
    'The Wise Wayfarers',
    'The Thoughtful Tacticians',
    'The Logical Learners',
    'The Rational Researchers',
    'The Analytical Adventurers',
    'The Clever Captains',
    'The Quick Queriers',
    'The Curious Commanders',
    'The Sharp Sages',
    'The Intrepid Investigators',
    'The Knowledgeable Knights',
    'The Intellectual Explorers',
    'The Problem-Solving Prodigies',
    'The Wise Wanderers',
    'The Thoughtful Trailblazers',
    'The Logical Leaders',
    'The Rational Revolutionaries',
    'The Analytical Avengers',
    'The Clever Commandos',
    'The Quick Quizmasters',
    'The Curious Consultants',
    'The Sharp Surveyors',
    'The Intrepid Instructors',
    'The Knowledgeable Knaves',
    'The Intellectual Investigators',
    'The Problem-Solving Paragons',
    'The Wise Warriors',
    'The Thoughtful Thespians',
    'The Logical Legends',
    'The Rational Rangers',
    'The Analytical Astronauts',
    'The Clever Chemists',
    'The Quick Quartet',
    'The Curious Counselors',
    'The Sharp Scholars',
    'The Intrepid Investigators',
    'The Knowledgeable Keepers',
    'The Intellectual Innovators',
    'The Problem-Solving Pioneers',
    'The Wise Wayfarers',
    'The Thoughtful Trailblazers',
    'The Logical Leaders',
    'The Rational Revolutionaries',
    'The Analytical Avengers',
    'The Clever Commandos',
    'The Quick Quizmasters'
]

def get_random_team_name():
    return random.choice(random_team_names)
