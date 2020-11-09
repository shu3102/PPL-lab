	.file	"A-1.c"
	.text
	.comm	Z, 4, 2
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$64, %rsp
	.seh_stackalloc	64
	.seh_endprologue
	call	__main
	movl	$6, -4(%rbp)
	movl	$10, -8(%rbp)
	movl	$20, -12(%rbp)
	movl	-8(%rbp), %eax
	imull	-12(%rbp), %eax
	addl	$25, %eax
	movl	%eax, -16(%rbp)
	movl	$6, -4(%rbp)
	leaq	Z(%rip), %rax
	movl	(%rax), %eax
	movl	%eax, -20(%rbp)
	nop
	addq	$64, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (GNU) 9.3.0"
