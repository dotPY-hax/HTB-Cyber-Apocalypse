#  The Chasm's Crossing Conundrum

This "hard" challenge is a little game/programming challenge
> As you and your trusty team of local pyramid experts stand at the precipice of the chasm, you catch a glimpse of the otherworldly relic glowing tantalizingly in the distance. But the final obstacle looms ahead - a narrow, unstable bridge that threatens to send you all tumbling into the depths below. It won't hold all of you at once. Time is running out, and the charge on your flashlight is dwindling. The chasm seems to be closing in, as if it's trying to swallow you whole. With each step, you feel the weight of the task at hand. The fate of your team, and perhaps even the world, rests on your shoulders. Can you summon the courage and skill to make it across in time, and claim the relic that lies just beyond your grasp?

![image](https://user-images.githubusercontent.com/67259802/227708191-cda67260-690e-40e1-82c2-31eb23d8560b.png)


![image](https://user-images.githubusercontent.com/67259802/227708256-d41580c6-5042-43ee-80f0-0e49af187b15.png)

Fortunately this is the well known Torch and Bridge problem just a bit more "blown up" since in its traditional form it only uses 4 people.

[Being a well known problem there is always someone on the internet who wrote a generalized solver for it in Haskell.](https://github.com/lenguyenthedat/general-bridge-and-torch-problem-solver)

Unfortunately I know very little Haskell so I have to improvise adapt and overcome.

I install Haskell on my box and grab the [Torchsolver.hs](https://github.com/lenguyenthedat/general-bridge-and-torch-problem-solver/blob/master/TorchSolver.hs)

This makes the challenge an easy wrapper writing and io parsing difficulty...
I establish a connection via a socket, grab the challenge question, parse it into a command understood by the general solver, parse the output of the solver back into the input format of the challenge and then send it back over the socket.
![image](https://user-images.githubusercontent.com/67259802/227709324-71eadc22-d78f-455f-bfdd-8e5d31a5645d.png)

[The simple wrapper code is here](https://github.com/dotPY-hax/HTB-Cyber-Apocalypse/blob/main/wrapper.py)

![image](https://user-images.githubusercontent.com/67259802/227709569-26b57935-8138-445c-9e60-e58d6588bd88.png)
