.text


main:
    and $t1, $t1, $zero
    addi $t1, $t1, 5
    and $t0, $t0, $zero
    addi $t0, $t0, 1
    slt $t3, $t1, $t0 #t3 should be 0 since 5 < 1 is not true
    slt $t4, $t0, $t1 #$t4 should be 1 since 1 < 5 is true

exit:
    beq $zero, $zero, exit



# ANSWER
# $t0 = 1
# $t1 = 5
# $t3 = 0
# $t4 = 1
