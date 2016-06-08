# associativememoryNN
A simple python code implementing associative memory neural network to train and store 4 digits.

Write a computer program to implement an auto associative neural net using the Hebb rule to set the weights (outer products). The program should read input from a 7×5 array into an x vector ( a 35 tuple) and should have a training mode in which the weights are set (outer products). The number of inputs may be specified in advance, but it will be more convenient to prompt the user interactively for more inputs. The program should also have a test mode in which the weights are not changed but the response of the net is determined. The response should be printed as a 7×5 array. It is good practice to display the input array, followed by the output array:

Try to answer the following questions:
i)	How many patterns can you store (and recall successfully)?
ii)	How much noise can your net handle?

.	.	#	.	.			.	#	#	#	.			.	#	#	#	.			.	.	.	.	#
.	#	#	.	.			#	.	.	.	#			#	.	.	.	#			.	.	.	#	#
.	.	#	.	.			.	.	.	.	#			.	.	.	.	#			.	.	#	.	#
.	.	#	.	.			.	.	.	#				.	.	#	#	.			.	#	.	.	#
.	.	#	.	.			.	.	#	.	.			.	.	.	.	#			#	#	#	#	#
.	.	#	.	.			.	#	.	.	.			#	.	.	.	#			.	.	.	.	#
.	#	#	#	.			#	#	#	#	#			.	#	#	#	.			.	.	.	.	#
