.text

main:
	ori $t4, $zero, 4
	ori $t5, $zero, 0
	ori $t1, $zero, 1
	sw  $t1, 0($t5)
	addi $t5, $t5, 4
	ori $t2, $zero, 1
	ori $t6, $zero, 13

loop:
	beq $t2, $t6, exit
	ori $t3, $zero, 0
	add $t7, $t2, $zero

multiplication:
	beq $t7, $zero, advance
	add $t3, $t3, $t1
	addi $t7, $t7, -1
	beq $zero, $zero, multiplication

advance:
	add $t1, $t3, $zero
	sw  $t1, 0($t5)
	addi $t5, $t5, 4
	addi $t2, $t2, 1
	beq $zero, $zero, loop

exit:
	beq $zero, $zero, exit

# ANSWER
# mem[0] = 1			# 0!
# mem[4] = 1			# 1!
# mem[8] = 2			# 2!
# mem[12] = 6			# 3!
# mem[16] = 24			# 4!
# mem[20] = 120			# 5!
# mem[24] = 720			# 6!
# mem[28] = 5040  		# 7!
# mem[32] = 40320		# 8!
# mem[36] = 362880		# 9!
# mem[40] = 3628800		# 10!
# mem[44] = 39916800	# 11!
# mem[48] = 479001600	# 12!
