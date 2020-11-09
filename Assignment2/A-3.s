	.file	"A-3.c"
	.text
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	movl	$0, -4(%rbp)
	jmp	.L2
.L3:
	sall	-4(%rbp)
.L2:
	cmpl	$99, -4(%rbp)
	jle	.L3
	movl	$0, -8(%rbp)
	jmp	.L4
.L7:
	movl	$0, -12(%rbp)
	jmp	.L5
.L6:
	movl	-8(%rbp), %eax
	imull	-12(%rbp), %eax
	addl	%eax, -4(%rbp)
	addl	$1, -12(%rbp)
.L5:
	cmpl	$49, -12(%rbp)
	jle	.L6
	addl	$1, -8(%rbp)
.L4:
	cmpl	$24, -8(%rbp)
	jle	.L7
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (GNU) 9.3.0"
