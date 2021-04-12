
# callgrind format
version: 1
creator: callgrind-3.13.0
pid: 6254
cmd:  ./prime-ex
part: 1


desc: I1 cache: 
desc: D1 cache: 
desc: LL cache: 

desc: Timerange: Basic block 0 - 1148523
desc: Trigger: Program termination

positions: line
events: Ir
summary: 7805388


ob=(5) /home/student/Documents/ASC/lab6/prime-ex
fl=(94) ???
fn=(354) 0x0000000000000640
0 17

fn=(368) FindPrimes
0 6012
cfn=(370) TestForPrime
calls=2000 0 
0 7258430
0 11700
cfn=(372) ShowProgress
calls=550 0 
0 144565
0 7250
cfn=(372)
calls=1450 0 
0 184034
0 8006

fn=(340) _start
0 11
cob=(3) /lib/x86_64-linux-gnu/libc-2.27.so
cfi=(95) /build/glibc-S9d2JN/glibc-2.27/csu/../csu/libc-start.c
cfn=(342) (below main)
calls=1 137 
0 7684053

fn=(372)
0 70995
cob=(3)
cfi=(100) /build/glibc-S9d2JN/glibc-2.27/stdio-common/printf.c
cfn=(376) printf
calls=199 28 
0 251405
0 199
0 6000

fn=(488) 0x0000000000000570
0 8

fn=(348) __libc_csu_init
0 15
cob=(2) ???
cfi=(18) ???
cfn=(350) 0x00000000001084f0
calls=1 0 
0 6
0 8
cfn=(354)
calls=1 0 
0 17
0 11

fn=(366) main
0 9
cfn=(368)
calls=1 0 
0 7619997
0 902
cob=(3)
cfi=(100)
cfn=(376)
calls=100 28 
0 61104
0 100
0 406

fn=(474) 0x0000000000000600
0 8
cob=(2)
cfi=(18)
cfn=(480) 0x0000000000108530
calls=1 0 
0 75
0 1
cfn=(488)
calls=1 0 
0 8
0 3

fn=(370)
0 7258430

ob=(3)
fl=(89) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strrchr-avx2.S
fn=(324) __strrchr_avx2
43 1
+1 1
+2 1
+1 1
+3 1
+1 1
+1 1
+33 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+3 1
+1 1
+9 1
+1 1
+99 1
+1 1
+8 1
+1 1
+1 1
+1 1
+1 1
+2 1
+1 1
+1 1
+1 1
+1 1

fl=(72) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-sse4_2.h
fn=(238) strcspn
30 5
fi=(129) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcspn.c
-1 1
fe=(72)

fn=(270) strspn
30 5
fi=(130) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strspn.c
-1 1
fe=(72)

fn=(254) strpbrk
30 5
fi=(131) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strpbrk.c
-1 1
fe=(72)

fl=(103) /build/glibc-S9d2JN/glibc-2.27/libio/fileops.c
fn=(386) _IO_file_overflow@@GLIBC_2.2.5
747 642
+7 214
-8 1284
+8 853
+35 426
+3 420
+3 630
+1 630
+1 1050
+5 840
-45 2
+12 2
+9 4
+8 1
-4 1
+3 2
-2 2
-3 1
+1 2
+5 1
-1 1
+1 3
+3 1
-2 1
+2 1
+1 4
+1 4
+11 12
-12 4
cfn=(442) _IO_do_write@@GLIBC_2.2.5
calls=4 433 
* 322
-31 2
cfi=(104) /build/glibc-S9d2JN/glibc-2.27/libio/genops.c
cfn=(388) _IO_doallocbuf
calls=1 362 
* 63480
+1 6

fn=(384) _IO_file_xsputn@@GLIBC_2.2.5
1220 5136
+7 1284
-7 3852
+6 4926
+7 3930
+17 3
+4 1570
+4 783
+2 2349
-1 783
+1 783
-2 783
cfi=(120) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S
cfn=(454) __mempcpy_avx_unaligned_erms
calls=783 208 
* 13508
* 783
* 783
+4 1566
+18 1566
+10 11556
-40 3
+16 3
fi=(121) /build/glibc-S9d2JN/glibc-2.27/libio/libioP.h
870 9
+2 6
+1 6
fe=(103)
1266 9
cfn=(386)
calls=3 747 
* 63790
* 6
+6 6
+1 21
+2 6
+11 9
+1 12
cfi=(104)
cfn=(444) _IO_default_xsputn
calls=3 392 
* 668
* 9
-52 1570
+1 1570
+3 2349
+2 5559
-2 4489

fn=(442)
433 12
+1 1
-3 48
+11 6
+7 12
fi=(121)
873 6
fe=(103)
457 12
cfn=(462) _IO_file_write@@GLIBC_2.2.5
calls=3 1196 
* 135
* 3
+1 15
+6 3
-4 3
+4 3
-4 9
+1 6
+3 3
-2 3
-29 12
+1 24
+29 6

fn=(462)
1196 18
+2 18
+5 3
cfi=(122) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/write.c
cfn=(464) write
calls=3 27 
* 27
+1 6
+5 3
+1 3
-12 6
+5 15
+10 9
+3 27

fn=(392) _IO_file_stat
1169 1
+1 3
cfi=(106) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/fxstat.c
cfn=(394) _fxstat
calls=1 34 
* 10

fn=(526) _IO_file_sync@@GLIBC_2.2.5
807 4
+5 4
+2 1
+1 2
+15 2
+4 4

fn=(522) _IO_file_setbuf@@GLIBC_2.2.5
389 2
+1 1
cfi=(104)
cfn=(524) _IO_default_setbuf
calls=1 +89 
* 68
* 2
+4 2
-1 2
+2 3
+2 1
+1 2

fl=(107) /build/glibc-S9d2JN/glibc-2.27/malloc/malloc.c
fn=(428) tcache_init.part.4
2996 1
-9 1
+9 9
+1 3
cfn=(430) _int_malloc
calls=1 3531 
* 389
+1 1
-1 1
+1 1
+8 4
+7 2
+2 1
+1 2
-1 1
+1 78
+3 2

fn=(432) sysmalloc
2274 8
+20 1
+11 1
-11 1
+11 1
+1 4
fi=(109) /build/glibc-S9d2JN/glibc-2.27/malloc/arena.c
535 1
fe=(107)
2321 2
fi=(109)
535 1
fe=(107)
2321 2
+66 1
+1 3
+10 1
-9 1
+9 3
+6 4
+3 3
2724 2
+1 1
+5 2
+3 2
+5 1
-3 1
+3 1
-2 1
+2 3
+1 1
-1 1
-1 1
+4 1
-3 2
+1 1
+2 1
+6 9
2460 3
+19 2
-11 1
+11 1
-11 1
+21 4
cfi=(114) /build/glibc-S9d2JN/glibc-2.27/malloc/morecore.c
cfn=(434) __default_morecore
calls=1 46 
* 61
* 1
+1 1
+3 3
+3 4
+1 2
+46 2
+2 2
+6 1
-6 1
+6 1
-82 1
+10 2
+8 1
-8 1
+8 1
+67 4
+34 2
+6 3
+22 2
+1 5
+2 1
-2 1
+2 1
+1 4
cfi=(114)
cfn=(434)
calls=1 46 
* 25
+12 3
+48 1
+1 1
-2 1
+1 2
+12 1
-12 1
+1 1
+11 1
2544 2
-3 3
+99 2
+1 4

fn=(398) malloc
3038 3
+5 2
+1 2
+1 1
+46 3
-46 1
cfi=(108) /build/glibc-S9d2JN/glibc-2.27/malloc/hooks.c
cfn=(400) malloc_hook_ini
calls=1 29 
* 63347

fn=(430)
3531 12
+32 2
-32 2
+32 18
+4 12
+24 4
4141 18
3649 5
+62 31
+1 3
+20 2
-1 4
+1 2
-1 2
+1 4
-2 5
+6 3
+66 1
-40 2
3889 1
3741 1
+1 1
+20 2
+40 2
-60 2
-12 1
+6 3
+66 1
-40 2
3889 1
3741 1
+1 1
+20 2
+40 2
-60 2
-90 3
+2 1
-2 1
+2 2
+59 20
-62 13
3914 4
+2 4
+3 1
-3 1
+3 2
+68 4
+1 4
+1 4
+1 4
+1 4
+5 4
3730 2
3903 4
+97 6
+3 8
-3 6
+3 4
-3 2
4100 2
+3 2
-2 4
+2 5
+17 3
1887 1
4113 1
1887 2
4135 3
cfn=(432)
calls=1 2274 
* 237
+1 1
-1 1
+1 1
1887 3
4105 1
+3 2
-3 1
+1 1
+2 3
+2 1
-2 2
-1 1
+1 2
+2 2

fl=(88) /build/glibc-S9d2JN/glibc-2.27/misc/init-misc.c
fn=(320) __init_misc
31 2
-1 3
+1 4
+2 3
cfi=(89)
cfn=(324)
calls=1 +10 
* 33
* 1
+4 5
+1 3
+2 4

fl=(96) /build/glibc-S9d2JN/glibc-2.27/stdlib/cxa_atexit.c
fn=(344) __cxa_atexit
65 7
-26 2
+26 1
-26 5
+1 2
cfn=(346) __new_exitfn
calls=1 +44 
* 29
+2 2
+7 2
+3 1
-1 1
+2 1
+1 1
+1 4
+1 1
+11 6

fn=(346)
84 2
-6 2
+1 2
-1 1
+11 5
+2 3
-2 1
+10 2
-10 2
+45 1
+1 1
+4 4
-19 1
+1 2

fl=(70) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcmp.c
fn=(230) strcmp
38 4
+9 1

fl=(66) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/ifunc-avx2.h
fn=(268) wcslen
32 1
-2 1
+2 2
-2 3
fi=(132) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wcslen.c
-1 1
fe=(66)

fn=(234) wcschr
32 2
-2 2
+2 4
-2 6
fi=(133) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wcschr.c
+1 2
fe=(66)

fn=(220) wmemchr
32 2
-2 2
+2 4
-2 6
fi=(134) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wmemchr.c
+1 2
fe=(66)

fl=(69) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncmp.c
fn=(228) strncmp
38 4
+1 3
+9 1

fl=(104)
fn=(458) __overflow
217 398
+2 597
+2 199
fi=(121)
870 597
+2 398
+1 398
fe=(104)
221 199
+1 398
-1 199
cfi=(103)
cfn=(386)
calls=199 747 
* 6567

fn=(524)
479 2
fi=(121)
870 1
fe=(104)
479 3
fi=(121)
870 1
fe=(104)
479 3
+1 1
fi=(121)
870 1
+2 2
+1 2
fe=(104)
480 2
cfi=(103)
cfn=(526)
calls=1 807 
* 17
* 3
+2 2
+7 1
-7 1
+10 2
+2 1
-2 1
+1 3
+2 6
-11 1
348 1
485 1
-1 1
+1 1
348 3
+7 1
-5 1
+1 1
+4 2

fn=(440) _IO_setb
347 3
+1 4
+3 1
+2 4
-3 1
+3 2
+3 3

fn=(516) _IO_flush_all_lockp
749 11
+5 4
+1 11
+3 1
-8 1
+5 1
+3 1
-3 1
+3 1
fi=(121)
870 2
fe=(104)
762 1
fi=(121)
870 2
fe=(104)
769 1
fi=(121)
872 2
+1 2
fe=(104)
769 3
cfi=(103)
cfn=(386)
calls=1 -22 
* 128
+1 3
+2 6
-14 3
+16 3
-16 6
+3 3
-1 3
+1 3
+3 21
+14 9
+1 3
+4 12
-29 4

fn=(388)
362 2
-1 3
+3 4
+4 4
-3 1
fi=(121)
870 3
+2 2
+1 2
fe=(104)
365 2
cfi=(105) /build/glibc-S9d2JN/glibc-2.27/libio/filedoalloc.c
cfn=(390) _IO_file_doallocate
calls=1 78 
* 63455
* 2

fn=(514) _IO_cleanup
926 2
+3 1
-3 8
+3 1
cfn=(516)
calls=1 749 
* 252
-80 1
+80 1
-80 2
+1 11
+3 1
-3 1
+3 1
-3 1
+3 1
fi=(121)
+17 5
fe=(104)
+31 3
-48 9
+9 9
+2 6
+6 12
+8 2
+9 1
fi=(121)
-15 2
+1 2
fe=(104)
+14 4
cfi=(103)
cfn=(522)
calls=1 389 
* 83
+2 3
+4 5
+1 9
+11 9
+1 2
+35 12
-63 3
+2 2
+2 1
+1 1
-1 1
+2 3
-35 4
+21 4

fn=(444)
392 6
-3 15
fi=(121)
870 3
fe=(104)
389 3
fi=(121)
870 3
fe=(104)
389 15
fi=(121)
870 6
fe=(104)
417 39
fi=(121)
872 22
+1 22
fe=(104)
417 44
cfi=(103)
cfn=(386)
calls=11 747 
* 363
* 22
+2 22
-22 56
+25 3
-29 3
+29 21

fl=(114)
fn=(434)
46 2
+1 2
cfi=(115) /build/glibc-S9d2JN/glibc-2.27/misc/sbrk.c
cfn=(436) sbrk
calls=2 -15 
* 72
+2 6
+3 4

fl=(127) /build/glibc-S9d2JN/glibc-2.27/nptl/unregister-atfork.c
fn=(484) __unregister_atfork
28 8
+8 2
-8 6
+11 4
+82 12

fl=(90) /build/glibc-S9d2JN/glibc-2.27/ctype/ctype-info.c
fn=(326) __ctype_init
31 5
+2 1
+2 1
-4 1
+4 1
-4 1
+2 3
+2 2
+1 1

fl=(77) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strchr.c
fn=(256) index
40 2
-2 1
+2 2
-2 2
+11 1

fl=(100)
fn=(376)
28 3289
+4 299
+1 598
-1 1495
+1 897
cfi=(101) /build/glibc-S9d2JN/glibc-2.27/stdio-common/vfprintf.c
cfn=(378) vfprintf
calls=299 1244 
* 304436
+4 1495

fl=(120)
fn=(454)
208 783
+1 783
+1 783
+17 783
+1 783
+44 783
+1 783
+2 783
+1 783
+1 783
+1 783
+1 586
+1 586
+1 192
+1 192
+1 192
+2 192
+29 197
+1 197
+1 197
+1 197
+1 197
+3 394
+1 394
+1 394
+1 394
+1 394

fl=(91) /build/glibc-S9d2JN/glibc-2.27/libio/vtables.c
fn=(328) check_stdfiles_vtables
84 4
+1 3
+1 3
+2 1

fl=(105)
fn=(390)
78 8
+6 4
fi=(121)
870 3
+2 2
+1 2
fe=(105)
84 3
cfi=(103)
cfn=(392)
calls=1 1169 
* 14
* 2
+2 4
+11 4
+4 2
cob=(2)
cfi=(18)
cfn=(396) 0x0000000004c4f2c0
calls=1 0 
* 63360
* 1
+2 1
-1 2
+2 4
cfi=(104)
cfn=(440)
calls=1 347 
* 18
+1 1
+1 8
-15 1
fi=(135) /build/glibc-S9d2JN/glibc-2.27/libio/../misc/sys/sysmacros.h
-12 6
fe=(105)
+12 1
-2 2
+5 2

fl=(59) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-strcasecmp.h
fn=(262) strcasecmp_l
32 5
fi=(78) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcasecmp_l.c
-1 1
fe=(59)

fn=(282) strncasecmp_l
32 5
fi=(81) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncase_l.c
-1 1
fe=(59)

fn=(202) strcasecmp
32 5
fi=(60) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcasecmp.c
-1 1
fe=(59)

fn=(240) strncasecmp
32 5
fi=(73) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncase.c
-1 1
fe=(59)

fl=(99) /build/glibc-S9d2JN/glibc-2.27/setjmp/sigjmp.c
fn=(364) __sigjmp_save
29 1
-1 2
+1 2
+5 3

fl=(102) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strchr-avx2.S
fn=(382) __strchrnul_avx2
45 797
+2 797
+1 797
+1 797
+2 797
+1 797
+1 797
+4 797
+1 797
+1 797
+1 797
+1 797
+1 797
+1 797
184 797
+2 797
+7 797
+1 797

fl=(119) /build/glibc-S9d2JN/glibc-2.27/libio/iopadn.c
fn=(450) _IO_padn
37 376
+8 188
-8 1880
+7 376
+10 564
-13 376
+21 376
+2 188
fi=(121)
870 564
+2 376
+1 376
fe=(119)
64 752
cfi=(103)
cfn=(384)
calls=188 1220 
* 13590
+1 188
+3 2256

fl=(76) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/ifunc-wmemset.h
fn=(252) wmemset
32 4
-2 2
+2 4
-2 4
+5 2
-1 8
fi=(136) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wmemset.c
-3 2
fe=(76)

fl=(122)
fn=(464)
27 24
+1 3

fl=(118) /build/glibc-S9d2JN/glibc-2.27/stdio-common/_itoa.c
fn=(448) _itoa_word
168 1196
+2 598
+9 8650
+9 598

fl=(101)
fn=(378)
1244 4186
+31 897
+8 898
+4 1495
+11 1196
+11 299
fi=(117) /build/glibc-S9d2JN/glibc-2.27/stdio-common/printf-parse.h
108 598
fe=(101)
1309 897
fi=(117)
108 299
cfi=(102)
cfn=(382)
calls=299 -63 
* 5382
* 299
fe=(101)
1324 299
fi=(117)
108 299
fe=(101)
1324 1794
+1 3887
+3 299
fi=(137) /build/glibc-S9d2JN/glibc-2.27/stdio-common/../libio/libioP.h
870 897
+2 299
-2 299
+2 299
-2 299
+3 598
fe=(101)
1328 1794
cfi=(103)
cfn=(384)
calls=299 1220 
* 83117
* 598
1696 1495
+1 897
+3 3588
1283 596
+45 598
+4 897
+4 2392
-57 299
+34 299
-8 299
-59 598
1378 7470
-3 498
-5 498
-4 498
-1 498
-1 498
-1 498
-1 498
-1 498
-1 498
+15 498
-16 498
-1 498
-1 498
+14 498
-4 498
+8 498
-1 996
1696 1794
-36 498
+2 996
+8 498
fi=(117)
108 1992
cfi=(102)
cfn=(382)
calls=498 -63 
* 8964
* 498
fe=(101)
1674 498
fi=(117)
108 498
fe=(101)
1674 1494
fi=(137)
872 1494
+1 996
fe=(101)
1674 3486
cfi=(103)
cfn=(384)
calls=498 1220 
* 15362
* 3486
+2 498
-2 498
+2 1295
-34 4981
cfi=(118)
cfn=(448)
calls=299 168 
* 11042
* 7756
fi=(117)
73 199
+12 199
-12 199
+2 1194
fe=(101)
1642 2392
1324 1196
1642 5346
fi=(137)
872 897
+1 598
fe=(101)
1642 1495
cfi=(103)
cfn=(384)
calls=299 1220 
* 23975
* 5739
+1 870
-1 7453
cfi=(119)
cfn=(450)
calls=188 37 
* 22426
* 7093
cfi=(104)
cfn=(458)
calls=199 217 
* 9950
* 597
1498 597
+8 398
+17 398
+3 1592
fi=(117)
75 199
fe=(101)
1526 1194

fl=(124) /build/glibc-S9d2JN/glibc-2.27/stdlib/cxa_thread_atexit_impl.c
fn=(470) __call_tls_dtors
145 3
+1 4
+18 4

fl=(97) /build/glibc-S9d2JN/glibc-2.27/setjmp/../sysdeps/x86_64/bsd-_setjmp.S
fn=(360) _setjmp
30 1
+2 1
cfi=(98) /build/glibc-S9d2JN/glibc-2.27/setjmp/../sysdeps/x86_64/setjmp.S
cfn=(362) __sigsetjmp
calls=1 -6 
* 27

fl=(98)
fn=(362)
26 1
+9 1
+1 2
+1 1
+4 1
+1 1
+1 1
+1 1
+1 1
+2 2
+2 1
+1 1
+1 1
+2 2
+2 1
+8 1
cfi=(99)
cfn=(364)
calls=1 -34 
* 8

fl=(85) /build/glibc-S9d2JN/glibc-2.27/csu/../csu/init-first.c
fn=(314) _init
52 8
+3 3
+14 1
fi=(86) /build/glibc-S9d2JN/glibc-2.27/csu/../sysdeps/generic/dl-hash.h
-25 1
fe=(85)
+23 1
+1 1
fi=(86)
-23 1
fe=(85)
+24 1
fi=(87) /build/glibc-S9d2JN/glibc-2.27/csu/../sysdeps/unix/sysv/linux/x86_64/init-first.c
-33 4
fi=(86)
+7 1
+5 3
+14 4
-17 3
+3 9
+14 12
-17 9
+22 1
fi=(87)
-31 2
+2 2
-2 1
+2 2
cfi=(65) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/dl-vdso.c
cfn=(216) _dl_vdso_vsym
calls=1 -13 
* 17
+2 1
+4 1
-4 1
+4 1
-4 1
+1 2
+1 1
+2 1
cfi=(65)
cfn=(216)
calls=1 -19 
* 17
fe=(85)
+37 3
fi=(87)
-36 2
+1 1
fe=(85)
+35 1
cfi=(88)
cfn=(320)
calls=1 -50 
* 58
+3 1
cfi=(90)
cfn=(326)
calls=1 -53 
* 16
+5 6
-27 1
-7 1
+7 4

fl=(56) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-memmove.h
fn=(248) memcpy@@GLIBC_2.14
44 5
+4 2
-1 2
+12 2
+2 5

fn=(196) memmove
44 10
+4 4
-1 4
+12 4
+2 10

fn=(222) mempcpy
44 5
+4 2
-1 2
+12 2
+2 5

fl=(123) /build/glibc-S9d2JN/glibc-2.27/stdlib/exit.c
fn=(468) __run_exit_handlers
40 9
+5 1
-5 1
+5 2
+11 14
+3 2
+2 5
+16 2
+35 6
+2 2
-44 6
+2 1
+1 1
-1 1
+4 4
+1 6
+29 1
-3 1
+5 1
-2 2
+2 2
cob=(1) /lib/x86_64-linux-gnu/ld-2.27.so
cfi=(125) /build/glibc-S9d2JN/glibc-2.27/elf/dl-fini.c
cfn=(472) _dl_fini
calls=1 -78 
* 722
+1 1
+11 1
+1 1
-1 1
+1 1
+5 4
-73 1
+12 1
+1 4
+63 2
+1 11
cfi=(104)
cfn=(514)
calls=1 926 
* 481
* 3
+2 2
cfi=(128) /build/glibc-S9d2JN/glibc-2.27/posix/../sysdeps/unix/sysv/linux/_exit.c
cfn=(528) _Exit
calls=1 27 
* 5
-86 1
cfi=(124)
cfn=(470)
calls=1 +99 
* 11
* 1

fn=(466) exit
139 1
-1 1
+1 3
cfn=(468)
calls=1 -99 
* 1324

fl=(126) /build/glibc-S9d2JN/glibc-2.27/stdlib/cxa_finalize.c
fn=(482) __cxa_finalize
30 4
+3 2
-3 10
+3 2
-3 2
+3 10
+3 6
+4 14
-4 6
+58 10
+4 12
-4 6
+12 4
+1 4
cfi=(127)
cfn=(484)
calls=2 -79 
* 32
+2 8
+1 16

fl=(92) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86/cacheinfo.c
fn=(330) init_cacheinfo
488 7
+14 6
758 2
+2 1
+1 1
+2 1
-3 1
+5 1
-5 1
+4 3
+4 2
+3 2
+2 1
+1 1
+2 1
-3 1
+5 1
-5 1
+4 3
+9 1
+2 8
-2 1
+3 8
500 1
+4 1
-4 1
+4 1
cfn=(332) handle_intel.constprop.1
calls=1 259 
* 469
+2 1
-2 1
+2 1
cfn=(332)
calls=1 259 
* 515
+5 1
-5 1
+5 1
cfn=(332)
calls=1 259 
* 542
+8 1
-8 1
+8 1
+11 1
-20 1
+25 3
+4 2
+8 6
+3 2
+9 6
+14 2
+4 1
+3 1
+1 1
-4 1
+3 1
-3 1
+3 1
+6 8
-39 3
+3 9
+6 6
-6 3
+6 2
+3 20
+5 2
+4 1
+1 1
-1 3
691 4
+1 5
+4 2
+59 2
592 2
+8 1
+2 1
-2 6
+2 4
-2 1
+4 1
+23 2
-25 2
+2 6
+2 6
+3 2
+1 8
+2 4
+3 2
+5 1
+2 2
+1 1
-1 1
+2 1
-2 1
+1 2
+27 2
+1 1
+1 2
+2 1
-1 1
+1 1
-24 3
+4 2
+3 1
+2 4
+1 1
+5 2

fn=(334) intel_check_word.isra.0
132 12
+6 6
-10 18
+10 6
-10 6
+10 6
-10 6
+10 12
-10 6
+10 6
+2 6
-2 6
+2 18
250 12
140 24
+2 15
+2 30
+8 30
+51 24
+22 12
fi=(93) /build/glibc-S9d2JN/glibc-2.27/string/../bits/stdlib-bsearch.h
28 12
-1 24
+4 24
+1 12
fe=(92)
+87 24
fi=(93)
-88 138
+1 69
fe=(92)
+87 138
+3 81
fi=(93)
-93 252
+8 15
-8 36
fe=(92)
134 3
255 36
-91 9
+3 9
-6 13
+3 4
+9 4
+5 14
+1 10
+17 5
-32 15
+3 15
+4 14
+2 28
+2 14
+2 8
+4 3
+2 6
+2 3
+2 3
-2 3
+2 6
-2 3
+3 9
-2 12
+2 6
-24 2
+7 2
+2 4

fn=(332)
259 21
+2 3
-2 9
+5 9
+8 3
+1 3
-3 3
+5 12
+6 6
+5 3
-5 9
+5 3
+2 3
+1 3
-1 3
+5 18
cfn=(334)
calls=3 132 
* 1035
+2 6
+3 21
cfn=(334)
calls=3 132 
* 314
+2 6
+19 33

fl=(82) /build/glibc-S9d2JN/glibc-2.27/time/../sysdeps/unix/sysv/linux/x86/gettimeofday.c
fn=(286) gettimeofday
42 2
fi=(64) /build/glibc-S9d2JN/glibc-2.27/time/../sysdeps/generic/dl-hash.h
+2 1
+1 1
fe=(82)
-3 3
fi=(64)
+1 1
+5 3
+14 4
-17 3
+3 9
+14 12
-17 9
+22 1
fe=(82)
-25 6
cfi=(65)
cfn=(216)
calls=1 -17 
* 17
* 5

fl=(71) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-memset.h
fn=(232) memset
42 5
+4 2
-1 4
+12 2
+2 5

fl=(110) /build/glibc-S9d2JN/glibc-2.27/elf/dl-addr.c
fn=(404) _dl_addr
126 9
+2 1
-2 1
+5 1
-5 1
+5 2
cob=(1)
cfi=(2) /build/glibc-S9d2JN/glibc-2.27/elf/rtld.c
cfn=(52) rtld_lock_default_lock_recursive
calls=1 784 
* 2
+2 2
cob=(1)
cfi=(111) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86_64/dl-trampoline.h
cfn=(412) _dl_runtime_resolve_xsave
calls=1 -62 
* 1117
* 5
+2 3
30 1
+1 1
-1 1
+1 1
+3 2
+5 1
+6 1
-7 1
+2 3
+2 3
+3 1
+5 7
-6 2
+6 4043
+2 1010
+1 2020
-1 1
+1 2
+2 3664
+9 2052
+7 28
-2 28
+2 2353
-2 2297
+2 6003
-10 11625
+2 9300
+1 14806
+36 2
+1 1
+1 3
+3 2
+36 2
cob=(1)
cfi=(2)
cfn=(54) rtld_lock_default_unlock_recursive
calls=1 790 
* 2
+3 9
-27 1
+1 1
+20 2

fl=(109)
fn=(402) ptmalloc_init.part.0
289 2
+5 1
-5 3
+13 2
+6 1
fi=(107)
1816 2
fe=(109)
308 12
fi=(107)
1816 13
+1 1
-1 3
+1 11
-1 390
+1 30
-1 90
+1 331
fe=(109)
313 1
fi=(107)
1825 1
fe=(109)
313 4
fi=(107)
1817 7
+11 1
-11 4
+9 1
fe=(109)
313 1
fi=(107)
1828 1
fe=(109)
313 1
cob=(1)
cfi=(111)
cfn=(412)
calls=1 71 
* 1027
* 5
+1 4
cob=(1)
cfi=(9) /build/glibc-S9d2JN/glibc-2.27/elf/dl-tunables.c
cfn=(26) __tunable_get_val
calls=1 +59 
* 18
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +58 
* 19
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +57 
* 18
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +56 
* 18
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +55 
* 19
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +54 
* 18
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +53 
* 18
* 1
+2 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +51 
* 18
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +50 
* 18
* 1
+1 4
cob=(1)
cfi=(9)
cfn=(26)
calls=1 +49 
* 18
* 1
+71 2
+1 2
+4 2
-1 1
+1 4
-97 5
cfi=(110)
cfn=(404)
calls=1 126 
* 60426
* 2
+1 4

fl=(57) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-unaligned-ssse3.h
fn=(272) stpncpy
33 4
fi=(79) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/stpncpy.c
-2 1
fe=(57)

fn=(244) strcpy
33 4
fi=(74) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcpy.c
-4 1
fe=(57)

fn=(198) strncpy
33 4
fi=(58) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncpy.c
-4 1
fe=(57)

fn=(276) stpcpy
33 4
fi=(80) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/stpcpy.c
* 1
fe=(57)

fn=(206) strcat
33 4
fi=(61) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcat.c
-4 1
fe=(57)

fl=(106)
fn=(394)
34 1
-1 1
+1 1
+1 6
+4 1

fl=(75) /build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wcsnlen.c
fn=(250) wcsnlen
40 1
-2 1
+2 2
-2 2
+11 1

fl=(63) /build/glibc-S9d2JN/glibc-2.27/time/../sysdeps/unix/sysv/linux/x86/time.c
fn=(212) time
43 2
fi=(64)
+1 1
+1 1
fe=(63)
-2 4
fi=(64)
+5 3
+14 4
-17 3
+3 9
+14 12
-17 9
+22 1
fe=(63)
-24 6
cfi=(65)
cfn=(216)
calls=1 -18 
* 17
* 5

fl=(67) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-memcmp.h
fn=(224) bcmp
33 5
-1 2
+2 2
+1 3
fi=(68) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memcmp.c
-6 1
fe=(67)

fl=(108)
fn=(400)
29 5
fi=(109)
291 1
fe=(108)
30 1
fi=(109)
291 1
fe=(108)
30 1
fi=(109)
291 1
fi=(107)
3049 7
+3 1
-2 2
+2 3
+13 4
+2 3
cfn=(430)
calls=1 3531 
* 158
+1 1
-1 1
+1 6
-19 4
-56 5
cfn=(428)
calls=1 +3 
* 496
+62 3
+2 5
+1 3
fe=(108)
33 6
cfi=(109)
cfn=(402)
calls=1 289 
* 62626
* 1
fi=(107)
3044 2
fe=(108)

fl=(115)
fn=(436)
32 2
+8 2
-8 6
+8 9
+1 2
cfi=(116) /build/glibc-S9d2JN/glibc-2.27/misc/../sysdeps/unix/sysv/linux/x86_64/brk.c
cfn=(438) brk
calls=1 -10 
* 12
* 3
+3 4
+4 6
+12 5
-4 2
cfi=(116)
cfn=(438)
calls=1 -25 
* 12
* 2
+4 5

fl=(128)
fn=(528)
27 2
+4 1
+2 2

fl=(62) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-avx2.h
fn=(258) strlen
32 1
-2 1
+2 2
-2 3
fi=(138) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strlen.c
-1 1
fe=(62)

fn=(280) strchrnul
32 1
-2 1
+2 2
-2 3
fi=(139) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strchrnul.c
+1 1
fe=(62)

fn=(236) strnlen
32 2
-2 2
+2 4
-2 6
fi=(140) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strnlen.c
+1 2
fe=(62)

fn=(260) memrchr
32 1
-2 1
+2 2
-2 3
fi=(141) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memrchr.c
-1 1
fe=(62)

fn=(218) rawmemchr
32 1
-2 1
+2 2
-2 3
fi=(142) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/rawmemchr.c
+1 1
fe=(62)

fn=(210) rindex
32 1
-2 1
+2 2
-2 3
fi=(143) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strrchr.c
-2 1
fe=(62)

fn=(266) memchr
32 1
-2 1
+2 2
-2 3
fi=(144) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memchr.c
-1 1
fe=(62)

fl=(116)
fn=(438)
31 16
+8 2
-6 4
+7 2

fl=(65)
fn=(216)
25 20
+1 8
+4 8
+18 24
-21 4
+20 4

fl=(95)
fn=(342)
137 8
+4 1
-4 2
+4 2
+98 1
-98 1
+98 1
+1 4
cfi=(96)
cfn=(344)
calls=1 65 
* 65
+22 4
+3 2
+1 5
cob=(5)
cfi=(94)
cfn=(348)
calls=1 0 
* 57
+4 4
+15 2
+12 2
cfi=(97)
cfn=(360)
calls=1 30 
* 29
+1 2
+5 2
+1 2
+3 2
+3 6
cob=(5)
cfi=(94)
cfn=(366)
calls=1 0 
* 7682518
+34 2
cfi=(123)
cfn=(466)
calls=1 139 
* 1329

ob=(2)
fl=(18)
fn=(502) 0x0000000004a2c560
0 1
cob=(3)
cfi=(126)
cfn=(482)
calls=1 30 
0 74

fn=(512) 0x0000000004a2c7a8
0 3

fn=(304) 0x0000000004a2c520
0 6

fn=(396)
0 1
cob=(3)
cfi=(107)
cfn=(398)
calls=1 3038 
0 63359

fn=(350)
0 6

fn=(88) 0x0000000004000f00
0 3
cob=(1)
cfi=(19) /build/glibc-S9d2JN/glibc-2.27/elf/dl-minimal.c
cfn=(90) free
calls=3 111 
0 12

fn=(480)
0 1
cob=(3)
cfi=(126)
cfn=(482)
calls=1 30 
0 74

fn=(494) 0x0000000000108884
0 3

ob=(1)
fl=(42) /build/glibc-S9d2JN/glibc-2.27/misc/../sysdeps/unix/sysv/linux/mmap64.c
fn=(132) mmap
51 14
+3 7
-6 84
+6 7
+5 70
+2 49
-7 12

fl=(53) /build/glibc-S9d2JN/glibc-2.27/elf/dl-version.c
fn=(172) _dl_check_all_versions
362 5
+2 1
-2 3
+4 3
+2 24
cfn=(174) _dl_check_map_versions
calls=4 156 
* 2320
-2 4
+2 16
-2 8
+5 7

fn=(174)
156 28
+15 12
+2 20
+2 4
+1 4
+2 4
-3 4
+1 4
+2 4
+3 6
-16 2
-8 4
+28 2
-4 2
+4 4
+16 2
37 4
201 2
37 10
+1 5
-1 10
+2 21
cfi=(36) /build/glibc-S9d2JN/glibc-2.27/elf/dl-misc.c
cfn=(116) _dl_name_match_p
calls=7 282 
* 638
* 14
209 6
+5 2
-71 6
+71 4
-71 6
+79 2
-2 2
-2 4
+4 2
-4 14
+4 1
-2 1
-2 2
+4 1
-4 12
57 3
+8 3
-8 6
+8 6
+6 9
+16 3
+1 6
+2 3
+5 18
+14 20
+12 21
+4 7
-30 14
225 12
+3 9
+5 1
-11 1
111 3
+3 12
cfi=(21) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/strcmp.S
cfn=(56) strcmp
calls=3 +30 
* 131
* 16
237 8
+14 6
+3 8
+3 12
+3 8
+4 2
-7 8
+3 6
+4 30
-7 120
+3 92
+8 9
+89 36
-83 12
cfi=(19)
cfn=(42) calloc
calls=3 92 
* 81
* 3
+1 3
-2 3
+2 3
+13 3
+2 3
-5 3
+3 3
+2 3
-2 3
+2 3
+3 8
+4 6
+18 1
-15 3
+2 3
-2 6
+2 6
+2 3
+1 3
-1 6
+1 3
-1 3
+1 3
+1 3
-2 3
+2 6
+1 9
+3 9
+8 6
+10 9
+3 8
+4 32
+6 32
+1 32
+1 32
-1 96
+1 32
-1 32
+1 32
+1 32
+3 96
+4 32
-14 68
+10 6
-96 2
-86 2
-8 2
+94 3

fl=(16) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/memcmp.S
fn=(36) bcmp
28 4
+1 4
+1 4
+1 4
+1 4
+1 4
+1 4
+1 4
+3 4
+1 4
+1 3
+1 3
+1 3
+1 3
+1 3
+1 3
+1 3
+2 2
+1 2
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+2 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 1
+1 1
+1 1
+2 1
+1 1
+1 1
+1 1
+1 1
+1 1
+25 2
+4 2
+1 2
+15 2
+1 2

fl=(17) /build/glibc-S9d2JN/glibc-2.27/elf/dl-object.c
fn=(50) _dl_add_to_namespace_list
31 6
+2 3
-2 9
+2 6
cfi=(2)
cfn=(52)
calls=3 784 
* 6
+2 22
+3 15
+2 2
+2 2
+4 2
+4 2
-4 4
+1 2
+4 4
-4 2
+1 2
+3 2
-3 2
+2 2
cfi=(2)
cfn=(54)
calls=2 790 
* 4
-4 1
+4 1
-4 2
+1 1
+4 2
-4 1
+1 1
+3 1
-3 1
+2 1
cfi=(2)
cfn=(54)
calls=1 790 
* 2
-5 2

fn=(38) _dl_new_object
59 36
+1 3
-1 3
+1 6
cfi=(13) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/../strlen.S
cfn=(28) strlen
calls=3 +19 
* 66
+6 3
-6 6
+6 3
+7 3
-7 3
-6 3
+6 9
+2 6
+5 9
cfi=(19)
cfn=(42)
calls=3 +19 
* 147
* 3
+3 3
-3 3
+3 3
+4 3
+5 3
-6 3
+6 3
-5 3
+5 3
-5 3
+4 3
+1 6
-1 3
+1 3
cfi=(20) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S
cfn=(48) memcpy
calls=3 +44 
* 41
+10 3
-10 3
+10 3
-10 3
+10 3
-8 3
+8 6
+1 3
-1 3
+1 9
+3 3
-3 3
+3 3
+9 3
-7 3
+4 3
+3 8
+2 2
-2 2
+2 30
-2 30
+18 6
-6 3
+1 3
+5 3
-6 3
+6 9
+2 2
+3 2
-3 4
+3 2
+4 6
+4 5
+8 1
+3 1
+3 2
-3 1
+3 1
-3 2
+3 4
-3 2
+3 2
+2 2
+21 2
-21 2
cfi=(13)
cfn=(28)
calls=2 -76 
* 68
+4 2
-4 4
+17 2
-13 6
+64 2
+4 27
100 8
+39 6
+70 6
cfi=(20)
cfn=(74) mempcpy
calls=2 -93 
* 32
* 42
+6 40
-1 40
+1 42
-1 2
+1 6
+5 4
-96 1
+7 4
+32 4
cfi=(19)
cfn=(46) malloc
calls=2 50 
* 36
* 2
+1 2
-1 4
+1 2

fl=(33) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/strcspn.S
fn=(100) strcspn
30 1
+7 1
+1 1
+2 1
+1 1
+1 1
+1 1
+1 33
+3 2
+7 1
+1 1
+1 1
+1 1
+2 1
+1 1
+1 1
+1 1
+2 1
+1 1
+1 1
+9 3
+12 1
+2 1
+1 1
+1 1
-4 11
+2 11
+1 11
+1 11
+2 12
+1 12
+1 12
+2 12
+1 12
+1 12
+2 12
+1 12
+1 12
+2 1
+1 1
+1 1
+2 1
+7 1
+4 1

fl=(23) /build/glibc-S9d2JN/glibc-2.27/posix/../sysdeps/unix/syscall-template.S
fn=(64) uname
78 4
+1 1

fl=(31) /build/glibc-S9d2JN/glibc-2.27/elf/dl-debug.c
fn=(92) _dl_debug_initialize
49 8
+5 6
+5 2
-1 1
+1 2
+1 2
-1 1
+5 1
-14 4
+4 8
+4 1
-1 1
+1 4

fn=(96) _dl_debug_state
74 2

fl=(15) /build/glibc-S9d2JN/glibc-2.27/elf/dl-environ.c
fn=(34) _dl_next_ld_env_entry
29 5
+3 16
+13 56
-13 168
+2 120
+1 44
+5 4
-3 4
+3 4
+2 4
+7 1

fl=(35) /build/glibc-S9d2JN/glibc-2.27/setjmp/../sysdeps/x86_64/setjmp.S
fn=(110) __sigsetjmp
26 3
+9 3
+1 6
+1 3
+4 3
+1 3
+1 3
+1 3
+1 3
+2 6
+2 3
+1 3
+1 3
+2 6
+2 3
+4 3
+1 3

fl=(28) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memset-vec-unaligned-erms.S
fn=(76) memset
109 65
+6 13
+1 13
+1 6
+1 6
+2 4
+1 4
+2 4
+59 2
+1 2
+10 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+2 31
+1 31
+1 31
+1 31
+1 31
+1 31
+1 31
+1 2
+15 7
+1 7
+1 7
+1 6
+1 6
+1 2
+1 2
+24 1
+1 1
+2 1
+3 4
+1 4
+2 4
+3 2
+1 2
+2 2

fl=(113) /build/glibc-S9d2JN/glibc-2.27/elf/dl-open.c
fn=(418) _dl_find_dso_for_object
176 5
+4 6
+1 4
+1 12
+1 2
-2 6
+5 2
+4 7

fl=(41) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/fxstat.c
fn=(130) _fxstat
34 3
-1 3
+1 3
+1 18
+4 3

fl=(11) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/dl-sysdep.c
fn=(62) _dl_discover_osversion
45 4
+2 3
+85 5
-45 3
cfi=(23)
cfn=(64)
calls=1 -9 
* 5
* 1
+15 1
-15 1
+20 1
-1 1
+3 12
+4 3
-2 6
+2 10
+2 1
+1 2
-3 4
+7 3
-1 3
+4 3
-2 3
+2 10
+5 2

fl=(1) ???
fn=(0) 0x0000000000001090
0 2
cfi=(2)
cfn=(2) _dl_start
calls=1 444 
0 119108
0 14
cfi=(83) /build/glibc-S9d2JN/glibc-2.27/elf/dl-init.c
cfn=(302) _dl_init
calls=1 79 
0 2197
0 3
cob=(5)
cfi=(94)
cfn=(340)
calls=1 0 
0 7684064

fl=(24) /build/glibc-S9d2JN/glibc-2.27/elf/dl-load.c
fn=(114) _dl_map_object
2151 21
+8 3
-8 6
+8 3
+1 12
+3 42
+5 49
+2 21
cfi=(36)
cfn=(116)
calls=7 282 
* 777
* 14
+4 12
+1 18
+3 2
+1 2
+1 2
-1 2
+1 2
cfi=(21)
cfn=(56)
calls=2 144 
* 48
* 4
2462 27
2196 6
+10 6
-53 2
+89 4
-2 2
+2 2
cfi=(29) /build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/../strchr.S
cfn=(84) index
calls=2 24 
* 46
* 4
2393 5
cfn=(82) expand_dynamic_string_token
calls=1 375 
* 158
* 1
-2 1
+3 5
+4 9
cfn=(118) open_verify.constprop.7
calls=1 1653 
* 223
+3 2
-3 1
+3 3
+12 3
+46 1
+1 3
-1 1
+1 9
cfn=(126) _dl_map_object_from_fd
calls=1 863 
* 1353
-1 1
+1 3
-1 1
+1 9
cfn=(126)
calls=1 863 
* 1702
* 6
2242 1
+4 2
cfi=(13)
cfn=(28)
calls=1 79 
* 16
* 1
+2 1
-2 1
+2 1
+7 4
+36 12
cfn=(152) open_path
calls=1 2003 
* 1339
+6 2
-6 1
+6 3
656 3
2385 2
+28 4
+2 2
-95 1
-14 1
+14 1
+2 3
+4 2
cfi=(50) /build/glibc-S9d2JN/glibc-2.27/elf/dl-cache.c
cfn=(156) _dl_load_cache_lookup
calls=1 187 
* 1611
+2 1
-2 1
+2 1
+4 2
+8 3
+23 10
cfn=(118)
calls=1 1653 
* 235
+4 2
-4 1
+4 3
+1 2
-88 7
656 3
2290 2
+1 2
-32 1
+1 2
-1 3
+8 7
-3 3
656 3
+9 3
2279 3

fn=(152)
2003 8
+1 1
+6 1
-6 1
+6 1
+5 11
-7 1
-1 1
+8 7
+3 3
+9 4
+7 3
+1 1
-13 3
+12 1
cfi=(20)
cfn=(74)
calls=1 116 
* 12
* 1
+55 2
-22 6
-32 2
+32 24
-32 16
+3 16
+4 48
cfi=(20)
cfn=(74)
calls=8 116 
* 101
* 32
cfi=(20)
cfn=(74)
calls=8 116 
* 96
+3 16
+3 24
+3 72
cfn=(118)
calls=8 1653 
* 432
* 8
+2 40
+2 16
+89 9
-24 7
+7 1
-2 1
+2 3
+3 3
-13 2
-57 16
+1 64
+6 16
+2 16
-2 16
+2 16
cfi=(49) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/xstat.c
cfn=(154) _xstat
calls=8 34 
* 101
* 8
+3 8
-3 8
+1 1
+2 1
-2 1
+2 7
-37 2
+37 7
-37 14

fn=(78) fillin_rpath
444 7
+2 1
-2 9
+4 3
cfi=(19)
cfn=(80) strsep
calls=1 265 
* 238
* 3
cfi=(19)
cfn=(80)
calls=1 265 
* 6
* 6
+7 2
+2 3
cfn=(82)
calls=1 -82 
* 108
+4 1
-4 1
+4 1
+5 2
cfi=(13)
cfn=(28)
calls=1 79 
* 16
+1 2
+7 6
+9 17
+1 8
+57 2
cob=(2)
cfi=(18)
cfn=(88)
calls=1 0 
* 5
* 1
-39 2
+4 7
-1 1
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+3 3
+5 1
+1 2
-2 2
+2 1
cfi=(20)
cfn=(74)
calls=1 116 
* 12
+3 1
-2 1
-1 1
+1 1
+2 1
+6 4
+1 17
+1 1
-1 3
+1 1
-1 14
+1 8
-1 1
+1 1
-1 3
+1 1
-1 2
+4 1
-1 1
+1 1
-1 1
+1 1
+8 1
-1 1
+4 3
-37 2
-28 1
+5 4
+66 1
+3 9
-15 2

fn=(82)
375 16
233 4
375 2
233 2
cfi=(29)
cfn=(84)
calls=2 24 
* 70
+3 4
400 2
-11 2
+11 12
-11 2
cfi=(30) /build/glibc-S9d2JN/glibc-2.27/string/strdup.c
cfn=(86) strdup
calls=2 40 
* 150

fn=(148) _dl_dst_count
230 4
+3 2
-3 4
+7 2
-7 6
+3 2
cfi=(29)
cfn=(84)
calls=2 24 
* 70
+3 4
+20 18

fn=(66) _dl_init_paths
678 1
+13 2
-13 8
+13 3
cfi=(25) /build/glibc-S9d2JN/glibc-2.27/elf/dl-hwcaps.c
cfn=(68) _dl_important_hwcaps
calls=1 42 
* 711
+5 1
-5 1
+5 1
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+1 1
-2 1
+2 2
+8 1
-1 1
+1 4
-1 3
+4 4
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+2 1
-2 2
+2 1
+7 1
+10 1
-11 1
+12 1
+3 1
+1 1
-5 1
+3 1
+1 1
-1 1
+9 1
-20 1
+17 1
+3 1
-3 17
cfi=(28)
cfn=(76)
calls=4 109 
* 48
+3 27
-12 3
-2 3
+10 3
-7 3
-1 3
+4 3
-1 3
+1 3
+1 3
+3 3
+1 3
-4 3
+4 3
+14 1
-11 1
+6 1
+1 1
+5 2
+2 4
+2 3
+38 5
-19 1
-2 2
+2 2
+21 3
cfi=(13)
cfn=(28)
calls=1 79 
* 16
* 8
cfi=(20)
cfn=(48)
calls=1 129 
* 10
* 1
+5 4
-1 2
+2 56
-1 57
+5 1
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+1 1
-2 1
+2 1
+6 7
cfn=(78)
calls=1 444 
* 588
+3 3
+6 1
+4 8
-37 2

fn=(118)
1653 120
+39 10
-39 20
+39 38
+31 30
cfi=(37) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/lxstat.c
cfn=(120) open
calls=10 39 
* 184
+2 10
-2 10
+2 12
+11 2
+6 2
-5 6
+5 12
cfi=(39) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/read.c
cfn=(124) read
calls=2 27 
* 10
+2 4
+2 2
+2 2
-2 2
+2 2
+6 4
+16 18
1985 4
cob=(2)
cfi=(18)
cfn=(88)
calls=2 0 
* 10
* 2
1770 14
+74 4
+5 4
+2 8
+6 4
+11 4
+6 2
+1 2
-1 6
+1 6
+1 4
+20 8
1730 8
1896 72
+2 38
+13 6
+3 8
+28 12
-3 18
+15 2
+6 3
-3 1
+1 1
+3 1
-3 2
+1 1
-1 1
-1 1
+4 2
1705 8
1989 90
1770 2
1942 12
+3 2
-4 2
+4 4
+5 1
+1 4
-36 6

fn=(126)
863 22
+10 2
-10 2
+10 2
-10 6
+10 2
cfi=(31)
cfn=(92)
calls=2 49 
* 16
fi=(40) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/posix/dl-fileid.h
37 6
fe=(24)
873 2
fi=(40)
37 2
cfi=(41)
cfn=(130)
calls=2 -3 
* 20
* 4
+4 2
fe=(24)
889 2
fi=(40)
40 2
+1 2
fe=(24)
889 27
+1 10
fi=(40)
49 13
fe=(24)
1401 18
907 4
+24 8
+10 4
+22 8
+32 4
874 2
998 14
cfi=(17)
cfn=(38)
calls=2 59 
* 758
+1 2
-1 2
+1 2
+11 4
+5 2
-5 2
+1 2
+5 2
-5 2
+1 2
+2 2
-2 2
+2 4
+1 6
+20 2
-2 2
+2 18
+8 10
+97 2
1031 2
1140 2
1037 2
-1 2
-5 4
1140 6
-96 32
-1 102
+1 95
+6 4
+5 4
+1 8
+11 20
+5 32
+9 12
-1 12
+1 4
+1 8
+2 4
-2 4
+1 4
-1 4
+3 4
+4 4
-7 4
+3 4
-1 4
+5 4
+1 12
+5 2
-1 2
+1 2
-15 2
+14 2
+1 10
+10 2
-10 2
-1 2
+1 2
-15 2
+14 2
+1 10
+10 2
-44 2
+1 1
+46 3
+4 1
+1 1
+2 1
-1 1
-1 2
+1 1
+3 3
+1 1
+3 1
-3 1
+7 4
+6 1
cfi=(32) /build/glibc-S9d2JN/glibc-2.27/elf/../elf/dl-tls.c
cfn=(164) _dl_next_tls_modid
calls=1 51 
* 6
* 2
+1 1
+19 4
+1 4
+1 2
-6 4
+1 2
+8 8
1011 2
1165 2
1011 2
1165 2
+10 4
fi=(43) /build/glibc-S9d2JN/glibc-2.27/elf/./dl-map-segments.h
50 2
+6 2
fe=(24)
1175 8
fi=(43)
56 6
fe=(24)
1175 2
fi=(43)
50 2
fe=(24)
1175 4
fi=(43)
56 4
cfi=(42)
cfn=(132)
calls=2 -5 
* 74
+4 2
-4 2
+4 4
+3 4
+1 2
+2 2
-2 2
-1 2
+3 2
+14 4
fi=(45) /build/glibc-S9d2JN/glibc-2.27/elf/./dl-load.h
+10 8
+1 6
+2 8
fi=(43)
+11 16
+45 4
-59 20
+2 12
+2 18
cfi=(42)
cfn=(132)
calls=2 -43 
* 66
* 6
+16 2
+2 2
-2 2
+1 2
+2 2
-1 2
+1 2
-1 6
+8 6
+3 4
+8 14
cfi=(28)
cfn=(76)
calls=2 -22 
* 249
* 6
+6 4
+4 9
cfi=(42)
cfn=(132)
calls=1 -90 
* 33
+3 3
-71 20
cfi=(44) /build/glibc-S9d2JN/glibc-2.27/misc/../sysdeps/unix/syscall-template.S
cfn=(136) mprotect
calls=2 +5 
* 10
* 6
fi=(45)
+21 5
+2 1
-1 3
+1 1
-1 1
+1 2
-1 2
+3 4
fe=(24)
1187 8
+9 4
fi=(3) /build/glibc-S9d2JN/glibc-2.27/elf/get-dynamic-info.h
42 2
fe=(24)
1196 2
fi=(3)
42 2
+6 2
-2 2
+2 4
+15 2
+5 2
+3 2
-1 2
-3 2
-3 36
+10 8
-26 24
+16 35
+10 35
-26 105
+26 2
-26 6
+2 90
+13 40
+2 8
+16 4
+20 7
+1 8
+1 8
+1 8
+2 8
+5 8
+1 7
+1 8
+6 6
+5 4
+7 4
+1 6
+18 6
+5 1
+2 1
-2 1
+2 1
+2 2
+2 2
+3 6
+10 1
-8 4
+8 1
+5 2
+3 4
fe=(24)
1203 4
+15 6
+19 4
+2 10
+54 6
+1 2
+3 2
cfi=(46) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/close.c
cfn=(142) close
calls=1 27 
* 5
* 2
cfi=(46)
cfn=(142)
calls=1 27 
* 5
* 4
+9 4
+2 6
+2 2
-2 2
+2 2
+16 4
cfi=(6) /build/glibc-S9d2JN/glibc-2.27/elf/dl-lookup.c
cfn=(10) _dl_setup_hash
calls=2 939 
* 46
+4 4
+1 4
+17 4
+1 1
+8 1
-5 3
+5 2
-5 3
+5 1
+10 4
+10 6
cfi=(17)
cfn=(50)
calls=2 31 
* 82
+4 6
fi=(3)
68 8
+3 8
+1 2
+1 8
fe=(24)
424 2

fl=(112) /build/glibc-S9d2JN/glibc-2.27/elf/../elf/dl-runtime.c
fn=(414) _dl_fixup
66 4
+6 4
-6 2
+3 4
+3 6
-4 2
+5 2
+2 2
-2 10
+2 2
-2 2
+2 2
+5 4
+4 4
+4 2
+7 2
-7 4
+4 4
+1 8
+2 8
+7 4
-1 2
+1 2
+10 18
cfi=(6)
cfn=(190) _dl_lookup_symbol_x
calls=2 790 
* 1847
* 2
+4 10
+10 14
+16 2
-8 2
+8 6
+4 6
fi=(5) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86_64/dl-machine.h
+96 2
fe=(112)
-92 6

fl=(44)
fn=(136)
78 24
+1 6

fn=(298) munmap
78 4
+1 1

fl=(50)
fn=(162) _dl_cache_libcmp
141 22
+1 28
+2 256
+20 122
+2 228
+4 53
+1 53
-29 106
+32 9
-28 6
+6 3
+2 3
-1 3
-1 6
+1 3
-1 3
+2 9
+2 9
-3 3
+3 3
+2 6
+9 24

fn=(156)
187 9
+8 2
+3 3
+45 1
+6 2
+11 1
-2 1
fi=(51) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86/dl-procinfo.h
39 1
fe=(50)
258 2
fi=(51)
39 3
+3 3
cfi=(21)
cfn=(56)
calls=1 144 
* 24
* 2
fe=(50)
264 4
cfi=(9)
cfn=(26)
calls=1 373 
* 18
* 1
fi=(26) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/not-errno.h
28 2
fe=(50)
264 1
fi=(26)
28 2
fe=(50)
266 2
fi=(26)
32 3
fe=(50)
270 2
+15 1
-15 1
+15 122
cfn=(162)
calls=8 141 
* 599
* 82
cfn=(162)
calls=2 141 
* 215
* 6
cfn=(162)
calls=1 141 
* 144
* 7
-15 2
+1 3
-1 2
+15 3
-84 4
cfi=(36)
cfn=(158) _dl_sysdep_read_whole_file
calls=1 44 
* 107
+8 1
-8 1
+8 4
+1 7
+7 1
-3 1
+3 3
+3 1
+1 2
-1 1
+1 1
+1 8
+63 3
+16 2
+4 2
+8 3
cfi=(13)
cfn=(28)
calls=1 79 
* 34
* 2
+1 1
-1 4
+1 2
cfi=(20)
cfn=(48)
calls=1 129 
* 10
+1 2
cfi=(30)
cfn=(86)
calls=1 40 
* 80
+1 8
-19 7
-12 27
fi=(51)
42 3
fe=(50)
297 3

fn=(296) _dl_unload_cache
326 4
-1 1
+3 2
cfi=(44)
cfn=(298)
calls=1 78 
* 5
+1 1
+2 2

fl=(52) /build/glibc-S9d2JN/glibc-2.27/elf/dl-sort-maps.c
fn=(166) _dl_sort_maps
28 16
+2 2
-2 2
+2 2
+92 10
-88 10
+1 4
-1 2
-1 2
+1 8
+1 2
cfi=(28)
cfn=(76)
calls=2 +74 
* 30
* 32
+4 4
+3 2
-3 4
+1 6
+2 2
-7 4
+4 8
+3 4
-3 8
+1 12
+2 4
+12 36
+2 12
+1 8
-1 6
+1 6
+2 18
+1 12
+58 24
cfi=(28)
cfn=(76)
calls=4 -9 
* 64
* 16
-28 24
-36 12
+61 28
-25 9
-44 12
+69 2
+7 16

fl=(34) /build/glibc-S9d2JN/glibc-2.27/elf/dl-error-skeleton.c
fn=(108) _dl_catch_exception
175 6
+15 3
-3 6
+4 3
-3 3
-13 3
+19 3
-3 3
+3 3
-19 3
+13 3
+2 3
+4 3
cfi=(35)
cfn=(110)
calls=3 26 
* 60
* 9
+2 9
cfi=(48) /build/glibc-S9d2JN/glibc-2.27/elf/dl-deps.c
cfn=(150) openaux
calls=2 60 
* 5849
cfi=(2)
cfn=(112) map_doit
calls=1 588 
* 2152
+2 3
-1 3
+1 6
-1 3
+1 3
+9 12

fn=(168) _dl_receive_error
226 3
+1 1
+1 1
+3 1
+1 1
+2 2
cfi=(2)
cfn=(170) version_check_doit
calls=1 621 
* 2401
+2 1
+1 1
+1 4

fn=(104) _dl_catch_error
213 6
+2 2
-2 1
+2 2
cfn=(108)
calls=1 -40 
* 2203
* 1
+1 2
+1 1
+1 1
-1 1
+1 1
+2 5

fl=(9)
fn=(26)
373 102
+4 17
-4 66
+9 3
+1 3
-6 14
+22 85
+2 17

fn=(16) __GI___tunables_init
289 8
-9 3
150 4
-82 185
+6 60
-3 60
+3 5060
+4 120
+5 60
297 60
83 60
297 60
fi=(10) /build/glibc-S9d2JN/glibc-2.27/elf/dl-tunables.h
121 120
-1 45
+1 18
-1 11
+1 44
-1 55
fe=(9)
330 240
-12 6600
fi=(10)
120 2160
+1 2354
-1 252
fe=(9)
312 5340
68 120
364 8

fl=(46)
fn=(142)
27 12
+1 3

fl=(47) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/access.c
fn=(144) access
27 7
+4 1

fl=(111)
fn=(412)
71 2
+3 2
+2 2
+10 2
+6 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+4 2
+1 2
+3 2
+1 2
+2 2
+1 2
+1 2
+1 2
+1 2
+1 2
+2 2
+7 2
+1 2
+1 2
cfi=(112)
cfn=(414)
calls=2 -59 
* 2001
+1 2
+5 2
+1 2
+1 2
+2 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+2 2
+2 2
+4 2
+3 2

fl=(12) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/x86_64/brk.c
fn=(22) brk
31 7
+8 1
-6 2
+7 1

fl=(20)
fn=(48)
129 14
+6 14
+1 14
+1 8
+1 8
+5 5
+1 5
+1 5
+1 5
+5 5
275 6
+1 6
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+2 1
+22 5
+1 5
+1 5
+1 5
+1 5
+24 3
+1 3
+1 3
+1 3
+22 3
+1 3
+1 3
+1 3
+1 3
+1 3
+1 3
+1 3
+2 3

fn=(74)
116 26
+1 26
+1 26
+17 26
+1 26
+1 4
+1 4
+5 3
+1 3
+1 3
+1 3
+5 3
275 22
+1 22
+1 8
+1 8
+1 3
+1 3
+1 1
+4 1
+22 14
+1 14
+1 14
+1 14
+1 14
+3 5
+1 5
+1 5
+1 5
+1 5
+3 2
+1 2
+1 2
+1 2
+1 2
+10 1
+1 1
+1 1
+1 1
+22 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+1 1
+2 1

fl=(2)
fn=(2)
444 9
+19 4
fi=(3)
48 1
fe=(2)
463 1
fi=(5)
59 3
fi=(3)
-11 1
fe=(2)
489 1
-3 1
fi=(3)
48 1
+25 2
-3 1
-7 1
+5 1
+3 1
+2 1
-6 1
+3 1
-3 2
-3 16
+10 4
-26 12
+16 13
+10 13
-26 39
+26 1
-26 3
+2 36
+13 20
+2 4
+16 2
+20 4
+1 4
+1 4
+1 4
+2 4
+5 4
+1 4
+1 4
+6 3
+5 2
+7 3
+1 3
+8 3
+3 3
+4 2
+1 2
fe=(2)
500 2
393 1
507 1
393 1
cfi=(6)
cfn=(10)
calls=1 939 
* 23
+1 2
+1 2
+1 2
+1 2
+8 1
+9 1
-9 3
+9 1
-6 1
-3 1
+9 1
cfi=(7) /build/glibc-S9d2JN/glibc-2.27/elf/../elf/dl-sysdep.c
cfn=(12) _dl_sysdep_start
calls=1 88 
* 118076
* 1
+9 4
+3 1
+4 1
-4 1
+4 1
532 9
-27 27
fi=(4) /build/glibc-S9d2JN/glibc-2.27/elf/do-rel.h
84 1
+27 1
-28 1
+28 2
+1 2
fi=(5)
540 2
fi=(4)
112 76
fi=(5)
540 76
+1 39
fi=(4)
111 39
fi=(5)
541 39
fi=(4)
111 39
fi=(5)
541 39
fi=(4)
111 39
+5 2
+8 1
fi=(5)
335 1
+87 1
fi=(4)
124 2
+12 1
+3 1
-3 1
+3 1
-3 1
fi=(5)
301 1
fi=(4)
137 1
fi=(5)
301 1
fi=(4)
137 1
fi=(5)
301 1
fi=(4)
136 8
+3 8
-3 8
+3 8
-3 8
fi=(5)
301 8
fi=(4)
137 8
fi=(5)
301 8
fi=(4)
137 8
fi=(5)
301 8
+9 27
+3 9
-3 18
+3 27
+22 54
fi=(3)
68 4
fi=(4)
+56 28
fi=(5)
354 27
fi=(3)
71 4
+1 1
+1 2
fe=(2)

fn=(52)
784 5
+1 5

fn=(54)
790 5
+1 5

fn=(176) init_tls
687 1
-6 1
+2 2
+4 1
+10 4
cfi=(19)
cfn=(42)
calls=1 92 
* 27
* 1
+11 1
-15 1
+3 1
+6 1
+2 1
-11 1
+15 1
+2 1
-1 1
+1 15
+2 8
+4 1
+2 1
-2 1
-5 8
+9 2
+3 1
cfi=(32)
cfn=(178) _dl_determine_tlsoffset
calls=1 141 
* 66
+7 1
cfi=(32)
cfn=(180) _dl_allocate_tls_storage
calls=1 332 
* 375
+1 1
-1 1
+1 1
+6 1
+3 1
-3 1
+3 6
+3 1
+2 1
+1 3

fn=(32) dl_main
870 1
+17 1
-17 10
+17 1
+4 1
2471 1
870 1
+21 1
+1 1
2466 1
892 1
+5 1
2471 1
897 1
2464 2
+7 3
-4 1
+4 3
+2 2
cfi=(15)
cfn=(34)
calls=1 29 
* 22
* 8
cfi=(15)
cfn=(34)
calls=4 29 
* 404
* 15
+4 12
-2 4
+2 66
+1 29
-1 87
+3 8
+6 24
+76 3
+1 4
cfi=(16)
cfn=(36)
calls=1 28 
* 31
* 2
-56 4
+7 8
cfi=(16)
cfn=(36)
calls=2 28 
* 54
* 4
+2 3
2635 3
+32 3
907 3
1108 7
cfi=(17)
cfn=(38)
calls=1 59 
* 230
+2 1
-2 1
+2 1
+1 1
+1 1
+5 2
-5 1
+1 2
+4 1
cfi=(17)
cfn=(50)
calls=1 31 
* 33
+1 2
879 1
1147 1
-3 1
-5 1
+1 1
+2 1
+5 5
+56 2
876 1
1166 1
+22 1
+15 2
-55 24
-1 27
+1 47
1250 3
+3 2
+2 2
+2 3
+13 3
+3 2
-2 1
+2 1
-2 3
cfi=(21)
cfn=(56)
calls=1 144 
* 50
* 2
+7 1
+3 1
-5 1
+3 1
-3 1
+5 1
+1 2
+4 2
+2 2
fi=(3)
33 1
+9 2
+6 1
-2 1
+2 2
+15 1
+5 1
+3 1
+2 1
-3 1
-3 1
-3 1
-14 52
+13 24
+1 20
+10 5
-26 15
+16 20
+10 20
-26 60
+26 1
-26 3
+33 3
+20 3
+1 4
+1 4
+1 4
+2 4
+5 4
+1 4
+1 4
+6 3
+5 2
+7 2
+1 3
+18 3
+5 1
+2 1
-2 1
+2 1
+2 2
+2 2
+1 1
+2 3
+10 1
-8 3
+8 1
+5 2
+1 2
+2 2
fe=(2)
1293 2
cfi=(6)
cfn=(10)
calls=1 939 
* 23
+3 2
fi=(22) /build/glibc-S9d2JN/glibc-2.27/elf/setup-vdso.h
24 2
fe=(2)
1318 1
cfi=(11)
cfn=(62)
calls=1 45 
* 87
* 9
-6 5
1167 2
+9 1
-7 1
-3 1
+10 1
+18 2
-37 3
+1 1
-6 3
+1 1
fi=(3)
65 4
+3 4
fe=(2)
1203 2
-1 2
+1 4
-1 2
+2 4
+1 1
+3 2
+1 2
-1 2
+1 2
+1 2
+1 6
+1 2
+31 2
+1 2
+1 1
-6 2
+1 1
2521 4
cfi=(16)
cfn=(36)
calls=1 28 
* 18
* 2
fi=(3)
71 4
+1 1
+1 3
fe=(2)
1323 2
cfi=(24)
cfn=(66)
calls=1 678 
* 1744
+3 3
cfi=(31)
cfn=(92)
calls=1 49 
* 17
+7 1
-7 1
+2 1
+5 1
+3 3
+1 1
+3 1
-3 3
+1 2
+3 1
+5 1
-7 1
+7 1
+1 5
+17 2
+1 2
+5 1
-3 3
+2 1
+1 2
+5 2
+1 5
-1 2
+3 2
+1 2
+5 2
+6 4
+1 1
-2 1
885 1
1391 1
1570 1
cfi=(32)
cfn=(94) _dl_count_modids
calls=1 113 
* 4
* 1
+8 3
+3 2
+4 3
+5 2
+1 1
cfi=(31)
cfn=(96)
calls=1 74 
* 1
+1 1
+4 2
+15 3
+4 1
-2 1
+2 2
+2 3
+1 1
-1 2
+1 1
cfn=(98) handle_ld_preload
calls=1 837 
* 2531
* 1
+1 4
+2 2
+10 3
cfi=(47)
cfn=(144)
calls=1 27 
* 8
* 2
+77 1
-96 1
+96 3
+17 3
+1 1
-1 1
+1 2
-1 1
+1 5
cfi=(48)
cfn=(146) _dl_map_object_deps
calls=1 159 
* 7349
+1 4
+5 1
-3 2
+3 2
+1 7
-1 2
+1 9
-1 6
+4 3
+1 3
+1 1
+2 2
+1 5
-1 4
+1 6
-1 6
+47 2
+2 2
-1 1
-1 2
+2 4
cfi=(34)
cfn=(168)
calls=1 226 
* 2416
+10 1
+1 1
-1 1
+1 1
+1 1
cfn=(176)
calls=1 687 
* 542
* 1
+2 2
799 1
fi=(145) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/dl-osinfo.h
64 2
fe=(2)
801 1
fi=(145)
77 1
fe=(2)
810 1
+7 1
-5 1
1808 2
2038 3
2161 3
+7 1
+2 3
+1 1
-1 2
+2 10
+2 4
-2 8
+2 4
+5 8
+2 8
+6 4
+2 8
+1 24
cfi=(54) /build/glibc-S9d2JN/glibc-2.27/elf/dl-reloc.c
cfn=(182) _dl_relocate_object
calls=3 148 
* 70864
+4 10
+1 2
cfi=(32)
cfn=(290) _dl_add_to_slotinfo
calls=1 887 
* 20
* 1
-12 1
+1 1
-3 2
+29 4
+2 1
+7 3
cfi=(32)
cfn=(292) _dl_allocate_tls_init
calls=1 437 
* 149
+3 2
-25 4
+2 2
+6 1
-6 1
+6 1
+26 3
+2 4
+15 1
+2 1
-2 2
+3 1
-3 1
+3 1
-3 1
+3 3
cfi=(54)
cfn=(182)
calls=1 148 
* 6191
+1 4
+2 2
+8 1
cfi=(7)
cfn=(294) _dl_sysdep_start_cleanup
calls=1 260 
* 1
+4 2
+20 3
cfi=(31)
cfn=(92)
calls=1 49 
* 8
+1 1
-1 1
+2 1
cfi=(31)
cfn=(96)
calls=1 74 
* 1
+1 1
+4 1
cfi=(50)
cfn=(296)
calls=1 326 
* 15
+5 8
2094 1
+13 1
-9 1
-4 1
+10 1
-6 1
+6 1
+3 1
1753 1
+1 1
-1 2
+1 1
+2 1
+2 3
+2 1
-4 1
+4 2
+14 4
+1 2
+1 3
-64 5
+1 1
-1 3
+4 3
+1 1
+1 2
+1 2
+32 2
2565 3

fn=(170)
621 2
+2 4
cfi=(53)
cfn=(172)
calls=1 362 
* 2391
* 2
+4 2

fn=(98)
837 8
+1 1
-1 1
-75 1
+86 1
-86 4
+80 2
+3 3
cfi=(33)
cfn=(100)
calls=1 30 
* 218
* 1
+1 3
+9 1
121 1
857 2
121 2
859 2
-97 5
-10 1
+4 1
+1 1
+1 1
+2 1
+2 1
cfi=(34)
cfn=(104)
calls=1 213 
* 2226
* 1
+1 3
+8 4
+71 2
+21 9
-15 4
cfi=(20)
cfn=(48)
calls=1 129 
* 18
+1 2

fn=(112)
588 1
+2 1
-2 1
+3 2
-1 3
+1 3
cfi=(24)
cfn=(114)
calls=1 2151 
* 2138
* 1
+2 2

fl=(125)
fn=(472)
30 8
+20 3
-3 6
+3 4
+3 2
cfi=(2)
cfn=(52)
calls=1 784 
* 2
+2 1
+3 2
+2 8
+8 1
-3 1
+8 1
-5 6
+7 8
+2 8
+2 8
+1 4
+1 4
+4 4
-12 12
+14 6
+1 4
+6 3
cfi=(52)
cfn=(166)
calls=1 -66 
* 253
+10 2
cfi=(2)
cfn=(54)
calls=1 790 
* 2
+5 6
+2 1
+2 3
-2 3
+2 9
+3 8
+3 12
+4 4
+11 2
+1 2
-1 2
+2 2
-2 2
+2 2
+1 14
+1 2
cob=(4) /usr/lib/valgrind/vgpreload_core-amd64-linux.so
cfi=(84) ???
cfn=(496) 0x0000000000000600
calls=1 0 
* 95
cob=(5)
cfi=(94)
cfn=(474)
calls=1 0 
* 95
* 2
-1 6
+5 4
+1 6
cob=(2)
cfi=(18)
cfn=(512)
calls=1 0 
* 3
cob=(2)
cfi=(18)
cfn=(494)
calls=1 0 
* 3
+6 24
+16 8
-56 10
+62 6
+6 2
+7 8
-90 7
+26 6

fl=(83)
fn=(302)
79 11
+5 1
-4 1
+1 1
+3 2
+8 2
+25 2
+1 12
+1 12
-89 12
+9 3
-3 6
+3 9
+5 6
+5 2
+9 6
cob=(3)
cfi=(85)
cfn=(314)
calls=1 -6 
* 207
* 1
+4 2
+6 2
+2 2
-2 1
+3 1
-1 1
+1 5
+1 4
cob=(3)
cfi=(91)
cfn=(328)
calls=1 +12 
* 11
* 4
cob=(3)
cfi=(92)
cfn=(330)
calls=1 488 
* 1773
* 2
-1 4
+47 3
+7 8
-80 3
-5 3
-10 3
+57 2
-48 1
-3 2
+3 3
+5 3
+5 2
+9 7
cob=(2)
cfi=(18)
cfn=(304)
calls=1 -58 
* 6
* 1
+3 1
+1 2
+6 1
+2 2
-2 2
+3 8
+1 4
cob=(4)
cfi=(84)
cfn=(308) 0x0000000000000640
calls=1 -72 
* 17
-1 5

fl=(25)
fn=(68)
42 4
+1 1
-1 8
+1 4
-1 1
+1 1
cfi=(9)
cfn=(26)
calls=1 373 
* 18
* 1
+3 3
-3 1
+12 6
+1 3
+1 1
-2 1
+2 1
-2 5
+1 3
+1 1
-2 1
+2 1
-2 5
+10 3
fi=(26)
-37 4
fe=(25)
131 4
-2 1
+17 6
+3 2
329 9
69 3
+77 1
+20 1
-19 1
+36 10
+1 3
-1 2
+1 3
fi=(27) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86/dl-hwcap.h
57 6
fe=(25)
186 1
+1 1
cfi=(13)
cfn=(28)
calls=1 79 
* 16
+1 1
-1 1
+1 3
-5 1
+5 1
-5 1
+5 2
-5 5
+8 3
+2 1
+1 6
+4 1
+4 1
-3 1
-1 1
+4 2
+3 4
+4 3
+1 1
-1 5
+1 3
+2 3
+2 2
-1 1
+1 1
-1 1
+2 2
+7 2
+6 11
+1 4
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+1 1
-1 1
+1 3
+29 10
+3 6
+17 1
-10 1
+10 11
-4 2
-3 1
+3 1
cfi=(20)
cfn=(74)
calls=1 116 
* 16
* 2
-3 1
+3 1
cfi=(20)
cfn=(74)
calls=1 116 
* 16
* 6
+3 7
+1 12
+1 4
cfi=(20)
cfn=(74)
calls=1 116 
* 14
-2 1
+2 2
-2 1
+5 6
cfi=(20)
cfn=(74)
calls=2 116 
* 28
+2 2
-2 4
+2 5
-7 4
+12 1
+1 2
-1 9
+1 14
-1 18
+5 10
+4 3
-4 12
+4 33
+1 12
-1 12
+1 24
-2 12
+1 24
-1 39
+4 6
+5 1
-2 1
+2 1
-1 1
-1 2
+2 1
-1 1
+1 4
+2 6
+1 2
+3 2
-6 5
+13 8
+1 1
-1 2
+3 2
-3 3
+1 3
-1 6
+3 6
+3 3
+2 2
-15 2
-6 3
-42 2

fl=(21)
fn=(56)
144 186
+1 186
+2 186
+1 186
+21 186
+1 186
+1 110
+1 110
+1 97
+1 97
+1 97
+1 97
+21 97
+1 97
+1 97
+1 97
+1 97
+1 97
+1 97
+5 5
+1 5
+9 5
+1 5
+1 5
+1 5
+1 5
+1 5
+1 5
+1 5
-7 89
+1 89
+1 89
+1 89
+1 89
+1 89
+1 89
+1 89
+1 31
+1 19
+1 19
+1 19
+2 19
+1 19
+1 19
+1 19
+1 19
+1 19
-5 12
+1 12
+1 12
+1 12
+1 12
+1 12
+10 63
+1 63
+1 63
+2 63
+6 63
+1 63
+1 63
+1 63
+1 63
+5 63
+2 63
+1 63
+1 126
+8 63
+1 63
+3 63
+1 63
+1 63
+1 63
+1 63
+1 63
946 2
+1 2
+1 2
+1 2
+1 2
+2 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 1
+4 1
+1 1
+1 1
+6 1
+1 1
+1 2
+4 1
+1 1
+3 1
+1 1
+1 1
+3 1
+1 1
+1 1
+6 1
+1 1
+1 1
+1 1
+1 1
+1 1
+72 4
+1 4
+1 4
+1 4
+1 4
+2 4
+1 4
+1 4
+1 4
+1 4
+1 4
+1 4
+1 1
+4 1
+1 1
+1 1
+6 1
+1 1
+1 2
+4 1
+1 1
+3 1
+1 1
+1 1
+3 1
+1 1
+1 1
+6 1
+1 1
+1 1
+1 1
+1 1
+1 1
+72 3
+1 3
+1 3
+1 3
+1 3
+2 3
+1 3
+1 3
+1 3
+1 3
+1 3
+1 3
+1 1
+4 1
+1 1
+1 1
+6 1
+1 1
+1 2
+4 1
+1 1
+3 1
+1 1
+1 1
+3 1
+1 1
+1 1
+6 1
+1 1
+1 1
+1 1
+1 1
+1 1
+72 3
+1 3
+1 3
+1 3
+1 3
+2 3
+1 3
+1 3
+1 3
+1 3
+1 3
+1 3
1446 4
+1 4
+1 4
+1 4
+1 4
+2 4
+1 4
+1 4
+1 4
+1 4
+1 4
+1 4
+1 4
+4 4
+1 4
+1 4
+6 4
+1 4
+1 8
+4 4
+1 4
+3 4
+1 4
+1 4
+3 4
+1 4
+1 4
+6 4
+1 4
+1 4
+1 4
+1 4
+1 4
1696 2
+1 2
+1 2
+1 2
+1 2
+2 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+4 2
+1 2
+1 2
+6 2
+1 2
+1 4
+4 2
+1 2
+3 2
+1 2
+1 2
+3 2
+1 2
+1 2
+6 2
+1 2
+1 2
+1 2
+1 2
+1 2
+7 1
+1 1
+2 1
+1 1
+2 1
+1 1
+1 1
+3 1
+1 1
+1 1
+6 1
+1 1
+1 1
+1 1
+1 1
+1 1
+41 5
+1 5
+1 5
+1 5
+1 5
+2 5
+1 5
+1 5
+1 5
+1 5
+1 5
+1 5
+1 5
+4 5
+1 5
+1 5
+6 5
+1 5
+1 10
+4 5
+1 5
+3 5
+1 5
+1 5
+3 5
+1 5
+1 5
+6 5
+1 5
+1 5
+1 5
+1 5
+1 5
+72 6
+1 6
+1 6
+1 6
+1 6
+2 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 2
+4 2
+1 2
+1 2
+6 2
+1 2
+1 4
+4 2
+1 2
+3 2
+1 2
+1 2
+3 2
+1 2
+1 2
+6 2
+1 2
+1 2
+1 2
+1 2
+1 2
+72 2
+1 2
+1 2
+1 2
+1 2
+2 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
2200 79
+2 79
+1 79
+1 79
+1 79
-3 15
+1 15
+1 15
+1 15
+1 57
+5 19
+6 19
+1 19
+8 19
+1 19
-16 167
+6 167
+1 167
+8 167
+1 167

fl=(29)
fn=(84)
24 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 4
+4 4
+1 4
+1 4
+1 4
+2 4
+4 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+1 2
+52 2
+4 2
+1 2
+1 2
+1 2
+2 2

fl=(8) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86/cpu-features.c
fn=(24) get_common_indeces.constprop.1
48 2
+4 4
+3 3
+4 1
-4 1
+4 1
-4 1
+3 1
+1 2
+1 4
+1 4
+1 3
+1 2
+7 2
+1 7
+7 3
+4 2
+2 4
+40 2
+4 4
+1 2
+3 1
+7 1
-8 1
+4 1
+2 1
-2 1
+4 2
+3 2
+50 3
88 2
+3 3
+3 1
-3 1
+3 1
+2 3
+2 2
+7 3
-5 3

fl=(49)
fn=(154)
34 8
-1 8
+1 8
+1 48
+4 1
-4 28

fl=(13)
fn=(28)
79 14
+1 14
+1 14
+1 14
+1 14
+1 14
+1 14
+2 14
+2 14
+31 14
+1 14
+1 14
+1 14
+1 14
+1 8
+2 8
+4 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+1 6
+5 48

fl=(19)
fn=(42)
92 8
+8 8
-1 16
-3 8
+4 16
+3 8
cfn=(46)
calls=8 -53 
* 210
* 8

fn=(46)
50 87
+11 42
+3 21
-3 21
+3 42
-3 2
+3 1
-3 1
+3 86
-15 3
+20 4
+1 2
+2 1
+1 8
cfi=(42)
cfn=(132)
calls=1 -22 
* 35
+2 2
+2 3
+2 1
+3 1
-3 2
+4 1
+2 5
-2 21
-1 21
+3 42
-29 1
-1 1
+1 1
+1 2
-2 2

fn=(80)
265 4
+2 2
+1 4
+4 33
+7 84
-2 56
+13 1
+4 2
-7 14
-15 44

fn=(90)
111 12

fl=(14) /build/glibc-S9d2JN/glibc-2.27/elf/../misc/sbrk.c
fn=(30) sbrk
32 4
+8 6
+4 2
+16 5

fl=(36)
fn=(116)
282 190
+1 76
cfi=(21)
cfn=(56)
calls=38 144 
* 996
* 38
+1 38
-1 38
+3 38
+2 76
+6 35
+1 175
-3 39
-4 78
+1 126
cfi=(21)
cfn=(56)
calls=42 144 
* 1170
* 84
+6 3
-11 3
+11 12

fn=(158)
44 2
+3 1
-3 3
+3 1
-3 3
+3 1
cfi=(37)
cfn=(120)
calls=1 -8 
* 16
+1 2
+2 5
cfi=(41)
cfn=(130)
calls=1 -16 
* 10
* 2
+2 1
+3 1
-3 1
+3 1
+13 2
cfi=(46)
cfn=(142)
calls=1 -41 
* 5
+3 7
-14 6
cfi=(42)
cfn=(132)
calls=1 -6 
* 35
* 2

fl=(48)
fn=(146)
159 1
-1 1
+1 1
-1 4
+1 1
-1 2
+1 1
-1 2
+1 1
-1 2
+1 1
-8 1
+8 2
-14 1
+6 3
+24 1
-16 1
-16 1
+1 1
+1 1
+6 1
+24 2
-28 2
-2 1
+31 1
-33 3
+2 2
-1 1
+1 2
+6 3
+24 1
-24 1
+24 6
+4 1
+19 1
+2 2
-14 1
-1 1
+13 1
304 4
-91 1
-4 1
+4 5
-4 3
+4 6
+12 8
+2 2
+11 2
-5 2
-6 4
+5 2
+2 4
+1 4
+3 8
-32 2
+32 2
+66 6
-55 6
-2 2
+2 2
cfi=(34)
cfn=(108)
calls=2 -74 
* 5951
* 2
+1 4
+9 2
+2 4
+5 2
+6 2
+2 2
-8 4
+3 2
+1 2
+1 2
+1 2
+4 10
+4 4
+1 4
-43 204
+1 102
+6 8
cfi=(24)
cfn=(148)
calls=2 -15 
* 112
* 10
434 8
+2 6
+3 4
-1 2
cfi=(19)
cfn=(46)
calls=2 50 
* 36
* 2
+2 2
-2 2
+2 2
+4 8
-1 2
+1 2
cfi=(20)
cfn=(48)
calls=2 129 
* 20
+1 12
cfi=(20)
cfn=(48)
calls=2 129 
* 20
+4 2
-1 2
+5 22
283 147
460 6
+4 5
+11 4
-1 1
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+3 1
-3 1
+3 2
+5 7
+1 1
+2 5
+6 2
+4 3
-10 6
+6 6
+4 9
-10 9
+13 2
+51 3
+2 1
-1 1
+1 2
+35 7
cfi=(20)
cfn=(48)
calls=1 129 
* 10
+4 5
cfi=(52)
cfn=(166)
calls=1 28 
* 232
+3 1
+2 1
+1 1
+1 1
-2 1
+2 2
+7 3
+3 2
+3 8
225 8
-19 4
461 2
214 25
+2 2
+2 8
+2 26
456 9
-1 4
+1 9
199 2
573 6

fn=(150)
60 4
+7 2
-4 6
+1 2
-1 2
+1 2
-1 10
cfi=(24)
cfn=(114)
calls=2 2151 
* 5815
* 2
+5 4

fl=(6)
fn=(190)
790 900
555 90
790 360
555 270
-1 180
+2 90
-1 90
+1 270
-1 270
+1 1213
-1 1213
+1 3639
-1 3729
793 90
-1 90
+4 90
+4 90
-8 90
+1 90
+7 342
+5 270
+6 270
-7 990
+15 32
-8 48
+2 1170
cfn=(192) do_lookup_x
calls=90 338 
* 31606
+3 434
+25 180
+24 574
+31 82
+9 328
+14 246
+3 328
+5 82
+2 826
-86 48
+17 8
+1 16
+59 2

fn=(192)
338 630
+1 90
-1 540
+6 180
+12 90
+30 90
-41 90
+41 90
+35 180
-65 450
+14 855
+8 570
+1 855
+3 285
+1 570
+4 570
+3 570
-5 285
+5 855
+3 1995
-99 203
540 1420
+1 72
cfi=(36)
cfn=(116)
calls=24 282 
* 1800
* 96
+3 609
349 570
+3 570
+4 570
+4 570
+4 570
fi=(55) /build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/generic/ldsodefs.h
102 246
fe=(6)
503 164
+3 620
-60 10
+64 27
+12 492
+2 82
+24 720
-1 16
397 261
-1 174
+2 174
+2 87
90 261
375 87
90 87
374 87
90 87
400 174
90 174
413 288
-10 890
+2 328
+2 164
-1 246
78 574
+12 410
+3 254
cfi=(21)
cfn=(56)
calls=18 +51 
* 915
* 54
+5 82
-1 82
+1 82
+2 162
+19 81
+1 729
452 820
148 2
+2 5
+30 35
-59 405
cfi=(21)
cfn=(56)
calls=81 +23 
* 3673
* 405

fn=(10)
939 12
+4 4
+4 8
+2 4
-1 4
+3 12
+1 4
+1 4
+3 4
-3 4
+7 4
-4 4
-1 4
+3 4
+2 4
-7 4
+7 4
+1 4

fl=(54)
fn=(182)
148 40
+15 4
-15 8
+15 4
+1 20
+6 12
+6 16
+1 8
-19 6
+22 6
+7 4
-32 4
+32 4
+44 4
fi=(5)
76 4
fe=(54)
231 8
fi=(5)
76 12
fe=(54)
258 146
-99 2
fi=(5)
481 6
fe=(54)
159 4
+99 2
fi=(4)
48 2
fe=(54)
258 2
fi=(4)
47 2
+11 2
-11 2
+11 2
-11 2
+11 2
fe=(54)
258 2
-99 2
fi=(5)
481 6
fe=(54)
159 4
+99 2
fi=(4)
48 2
fe=(54)
258 2
fi=(4)
47 2
+11 2
-11 2
+11 2
-11 2
+11 2
fe=(54)
258 4
fi=(4)
48 4
fe=(54)
258 4
fi=(4)
47 4
+11 4
-11 4
+11 4
-11 4
+11 4
+26 6
+14 12
-15 12
+3 24
+12 6
+10 8
+10 18
+6 5
-3 10
+3 5
fi=(5)
491 3
fi=(4)
51 3
fi=(5)
491 3
fi=(4)
50 6
+77 412
+12 206
-3 309
fi=(5)
276 103
fi=(4)
139 103
-2 103
-1 103
+1 103
+1 103
-1 206
fi=(5)
276 103
+21 206
+4 206
+7 412
fi=(55)
102 258
fi=(5)
308 1655
fi=(4)
138 83
fi=(5)
308 166
fi=(4)
138 83
fi=(5)
308 83
fi=(4)
138 83
fi=(5)
308 1162
cfi=(6)
cfn=(190)
calls=83 790 
* 46476
* 498
+2 258
+25 618
fi=(4)
74 4
+1 7
+1 78
fi=(5)
551 39
+24 78
+2 39
cob=(3)
cfi=(82)
cfn=(286)
calls=1 42 
* 77
cob=(3)
cfi=(59)
cfn=(282)
calls=1 32 
* 6
cob=(3)
cfi=(62)
cfn=(280)
calls=1 32 
* 8
cob=(3)
cfi=(57)
cfn=(276)
calls=1 33 
* 5
cob=(3)
cfi=(57)
cfn=(272)
calls=1 33 
* 5
cob=(3)
cfi=(72)
cfn=(270)
calls=1 30 
* 6
cob=(3)
cfi=(66)
cfn=(268)
calls=1 32 
* 8
cob=(3)
cfi=(62)
cfn=(266)
calls=1 32 
* 8
cob=(3)
cfi=(59)
cfn=(262)
calls=1 32 
* 6
cob=(3)
cfi=(62)
cfn=(260)
calls=1 32 
* 8
cob=(3)
cfi=(62)
cfn=(258)
calls=1 32 
* 8
cob=(3)
cfi=(77)
cfn=(256)
calls=1 40 
* 8
cob=(3)
cfi=(72)
cfn=(254)
calls=1 30 
* 6
cob=(3)
cfi=(76)
cfn=(252)
calls=2 32 
* 26
cob=(3)
cfi=(75)
cfn=(250)
calls=1 40 
* 7
cob=(3)
cfi=(56)
cfn=(248)
calls=1 44 
* 16
cob=(3)
cfi=(57)
cfn=(244)
calls=1 33 
* 5
cob=(3)
cfi=(59)
cfn=(240)
calls=1 32 
* 6
cob=(3)
cfi=(72)
cfn=(238)
calls=1 30 
* 6
cob=(3)
cfi=(62)
cfn=(236)
calls=2 32 
* 16
cob=(3)
cfi=(66)
cfn=(234)
calls=2 32 
* 16
cob=(3)
cfi=(71)
cfn=(232)
calls=1 42 
* 18
cob=(3)
cfi=(70)
cfn=(230)
calls=1 38 
* 5
cob=(3)
cfi=(69)
cfn=(228)
calls=1 38 
* 8
cob=(3)
cfi=(67)
cfn=(224)
calls=1 33 
* 13
cob=(3)
cfi=(56)
cfn=(222)
calls=1 44 
* 16
cob=(3)
cfi=(66)
cfn=(220)
calls=2 32 
* 16
cob=(3)
cfi=(62)
cfn=(218)
calls=1 32 
* 8
cob=(3)
cfi=(63)
cfn=(212)
calls=1 43 
* 77
cob=(3)
cfi=(62)
cfn=(210)
calls=1 32 
* 8
cob=(3)
cfi=(57)
cfn=(206)
calls=1 33 
* 5
cob=(3)
cfi=(59)
cfn=(202)
calls=1 32 
* 6
cob=(3)
cfi=(57)
cfn=(198)
calls=1 33 
* 5
cob=(3)
cfi=(56)
cfn=(196)
calls=2 44 
* 32
-26 39
+27 39
fi=(4)
75 121
fe=(54)
258 2
fi=(4)
75 14
fe=(54)
258 14
+3 16
+24 4
+3 8
+17 12
+8 20
+3 4
-3 4
+3 4
+4 8
+1 12
cfi=(44)
cfn=(136)
calls=4 78 
* 20
* 8
-14 32
fi=(5)
131 6
458 344
fi=(4)
124 309
+19 15
fi=(5)
430 51
+4 68
+5 17
+9 17
-9 34
+9 34
308 34
+5 17
-3 34
+3 133
-3 164
+3 246
-5 24
fi=(4)
61 4
-10 2
-1 4
fi=(5)
551 16
+4 16
+2 24
+1 8
fi=(4)
61 141
+2 188
+2 119
+46 9
fi=(5)
541 1244
fi=(4)
111 1244
fi=(5)
541 1244
fi=(4)
111 1244
fi=(5)
541 1244
fi=(4)
111 1244
fi=(5)
535 1244
fi=(4)
112 2488
fi=(5)
535 2488
+5 2488
fi=(4)
50 1
160 1
51 1
160 4
+2 20
+9 10
-1 5
+1 5
-1 10
fi=(5)
276 5
fi=(4)
170 15
fi=(5)
276 5
+21 10
+4 10
+7 20
fi=(55)
102 15
fi=(5)
308 170
cfi=(6)
cfn=(190)
calls=5 790 
* 2413
* 35
+2 15
+25 30
fe=(54)
-77 10
fi=(5)
82 4
+4 6
+14 2
-8 2
+8 4
+20 4
+4 8
-2 4
458 20
fi=(4)
160 17
+14 2
fi=(5)
313 1
-3 2
+3 3
-5 159
fe=(54)
180 3
fi=(5)
308 24
fe=(54)

fl=(30)
fn=(86)
40 12
+1 3
cfi=(13)
cfn=(28)
calls=3 +38 
* 84
* 3
+1 6
cfi=(19)
cfn=(46)
calls=3 +8 
* 54
* 3
+2 6
+4 3
-1 6
+1 6
-1 6
cfi=(20)
cfn=(48)
calls=3 +82 
* 38

fl=(32)
fn=(164)
51 4
+48 1
+4 1

fn=(178)
141 1
-6 5
+6 2
+3 2
+36 3
+2 4
-2 1
-2 1
-40 1
-1 1
-1 2
+69 2
+3 2
-3 5
+2 2
+10 1
-37 2
+25 1
-25 2
+5 1
-1 1
+5 2
-4 1
-1 2
+3 2
+2 3
-9 5
+93 1
-53 1
+1 1
+52 1
-1 1
+1 4

fn=(292)
437 8
+1 1
-1 1
+1 1
+4 1
+6 2
-6 1
+6 1
+12 1
-15 1
+39 1
-24 1
-16 2
+21 9
+6 15
+3 1
+1 2
+6 3
+3 1
-2 1
+6 1
-6 1
+2 1
+4 1
-4 2
+3 1
-3 1
+1 1
+2 1
+4 2
+1 4
+2 2
+1 2
+12 1
-3 1
+3 2
cfi=(20)
cfn=(74)
calls=1 116 
* 12
* 5
cfi=(28)
cfn=(76)
calls=1 109 
* 33
* 7
-42 2
+52 1
+4 3
+3 8

fn=(290)
887 4
+9 1
-3 2
+8 7
+41 1
+1 1
+1 4

fn=(94)
113 2
+1 2

fn=(180)
332 1
+2 1
-2 2
+13 1
+1 2
cfi=(19)
cfn=(46)
calls=1 50 
* 18
* 1
+1 3
+8 2
-69 1
+69 2
+1 1
+4 297
+19 1
-94 2
+1 2
cfi=(19)
cfn=(42)
calls=1 92 
* 27
* 1
+1 2
+3 1
+6 2
+89 5

fl=(37)
fn=(120)
39 11
fi=(38) /build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/open64.c
-3 11
+3 66
+8 77
+2 3
-2 24
+2 8
fe=(37)

fl=(39)
fn=(124)
27 8
+1 2

fl=(7)
fn=(294)
260 1

fn=(12)
88 8
+25 1
-1 1
+1 190
+6 1
-3 1
+1 1
-4 1
+3 1
+3 4
+1 2
-1 12
-29 1
-1 10
+30 2
+1 108
+3 1
-4 74
+62 1
-62 1
+63 1
-1 1
-62 3
+34 1
-34 2
+35 1
-35 2
+46 1
-46 1
+47 1
-1 1
-46 3
+40 1
-40 1
+41 1
-1 1
-40 3
+37 1
-37 2
+38 1
-38 3
+13 1
-13 2
+14 1
-14 2
+10 1
-10 2
+11 1
-11 2
+7 1
-7 4
224 1
cfi=(9)
cfn=(16)
calls=1 +65 
* 23107
fi=(11)
35 2
cfi=(12)
cfn=(22)
calls=1 -4 
* 11
fi=(8)
210 1
-12 1
+1 1
+11 1
+3 1
-3 1
+3 5
381 3
+1 1
+3 2
+1 1
+6 1
+5 2
-3 1
+3 1
-4 1
+4 1
cfi=(9)
cfn=(26)
calls=1 -24 
* 16
+2 4
cfi=(9)
cfn=(26)
calls=1 -26 
* 18
* 1
+2 3
-2 1
+2 1
cfi=(9)
cfn=(26)
calls=1 -28 
* 18
* 1
+2 3
-2 1
+2 1
cfi=(9)
cfn=(26)
calls=1 -30 
* 18
+12 1
-12 1
+11 1
-11 1
+12 1
fe=(7)
236 1
cfi=(13)
cfn=(28)
calls=1 79 
* 16
* 1
+2 2
cfi=(14)
cfn=(30)
calls=1 32 
* 17
* 3
+12 3
+3 5
cfi=(2)
cfn=(32)
calls=1 870 
* 94147
+1 1
+1 8
fi=(8)
419 3
+28 2
-9 3
+2 4
+1 2
+2 4
+1 2
219 6
cfn=(24)
calls=1 48 
* 87
37 2
+1 2
+1 6
224 4
327 4
+7 6
217 3
+9 2
+1 1
-1 1
+1 6
+46 3
+22 2
+10 5
+13 3
-13 2
fe=(7)

ob=(4)
fl=(84)
fn=(496)
0 8
cob=(2)
cfi=(18)
cfn=(502)
calls=1 0 
0 75
0 1
cfn=(506) 0x0000000000000570
calls=1 0 
0 8
0 3

fn=(506)
0 8

fn=(308)
0 17

totals: 7805388
desc: I1 cache:         32768 B, 64 B, 8-way associative
desc: D1 cache:         32768 B, 64 B, 8-way associative
desc: LL cache:         6291456 B, 64 B, 12-way associative
cmd: ./prime-ex
events: Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw 
fl=/build/glibc-S9d2JN/glibc-2.27/csu/../csu/init-first.c
fn=_init
52 8 1 1 0 0 0 4 0 0
55 4 1 1 1 1 0 1 0 0
62 5 1 1 4 0 0 0 0 0
67 1 0 0 0 0 0 1 1 1
68 1 0 0 0 0 0 1 0 0
69 2 0 0 1 1 0 1 1 1
81 4 0 0 0 0 0 1 0 0
84 1 0 0 0 0 0 1 0 0
89 6 0 0 5 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/csu/../csu/libc-start.c
fn=(below main)
137 10 1 1 0 0 0 7 0 0
141 4 0 0 1 0 0 1 0 0
239 2 1 1 0 0 0 0 0 0
240 4 0 0 0 0 0 1 0 0
262 4 0 0 2 0 0 0 0 0
265 2 0 0 0 0 0 0 0 0
266 5 1 1 4 0 0 1 0 0
270 4 0 0 2 0 0 0 0 0
285 2 0 0 0 0 0 0 0 0
297 2 0 0 0 0 0 1 0 0
298 2 0 0 0 0 0 0 0 0
303 2 1 1 1 1 0 1 0 0
304 2 0 0 1 1 0 1 0 0
307 2 0 0 0 0 0 1 0 0
310 6 0 0 5 0 0 1 0 0
344 2 0 0 0 0 0 1 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/csu/../sysdeps/generic/dl-hash.h
fn=_init
43 1 0 0 0 0 0 0 0 0
44 1 1 1 0 0 0 0 0 0
45 13 0 0 4 0 0 0 0 0
48 12 1 1 0 0 0 0 0 0
62 16 0 0 0 0 0 0 0 0
67 1 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/csu/../sysdeps/unix/sysv/linux/x86_64/init-first.c
fn=_init
36 7 0 0 0 0 0 3 0 0
38 4 1 1 0 0 0 1 0 0
40 3 0 0 0 0 0 0 0 0
41 2 0 0 1 0 0 0 0 0
42 1 0 0 0 0 0 1 0 0
44 3 0 0 0 0 0 1 0 0
45 2 0 0 1 0 0 0 0 0
46 1 0 0 0 0 0 1 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/ctype/ctype-info.c
fn=__ctype_init
31 7 1 1 5 2 0 1 0 0
33 4 0 0 2 1 0 1 0 0
35 4 1 1 2 0 0 1 0 0
36 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../elf/dl-runtime.c
fn=_dl_fixup
66 6 1 1 0 0 0 2 0 0
68 2 0 0 2 0 0 0 0 0
69 4 0 0 4 2 0 0 0 0
72 10 0 0 4 4 0 0 0 0
73 14 1 1 4 2 0 2 0 0
75 6 0 0 4 0 0 0 0 0
80 4 0 0 0 0 0 0 0 0
84 4 0 0 2 1 0 0 0 0
88 6 0 0 2 1 0 0 0 0
92 4 0 0 4 3 0 0 0 0
93 8 1 1 2 1 0 0 0 0
95 10 0 0 2 1 0 0 0 0
101 2 0 0 0 0 0 0 0 0
102 6 0 0 2 1 0 0 0 0
112 20 1 1 4 2 0 6 0 0
116 10 0 0 6 0 0 0 0 0
126 14 0 0 4 0 0 0 0 0
134 2 0 0 2 0 0 0 0 0
142 8 1 1 2 0 0 0 0 0
146 6 0 0 2 1 0 0 0 0
150 6 0 0 4 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../elf/dl-sysdep.c
fn=_dl_sysdep_start
88 8 1 1 0 0 0 6 1 1
89 10 1 1 4 1 1 5 0 0
90 1 0 0 0 0 0 0 0 0
112 1 0 0 0 0 0 1 0 0
113 192 1 1 62 8 8 4 3 3
116 2 0 0 0 0 0 1 0 0
117 1 1 1 0 0 0 1 0 0
119 126 5 5 32 6 6 13 1 1
120 110 0 0 18 3 3 0 0 0
123 1 0 0 1 0 0 0 0 0
126 1 1 1 1 0 0 0 0 0
129 1 1 1 1 0 0 0 0 0
130 1 0 0 0 0 0 0 0 0
132 1 0 0 1 0 0 0 0 0
133 1 0 0 0 0 0 0 0 0
153 1 1 1 1 0 0 0 0 0
154 1 0 0 0 0 0 0 0 0
156 1 0 0 1 0 0 0 0 0
157 1 0 0 0 0 0 0 0 0
159 2 2 2 1 0 0 1 0 0
160 1 0 0 0 0 0 1 0 0
165 2 0 0 1 0 0 1 0 0
166 1 0 0 0 0 0 1 0 0
181 2 1 1 1 0 0 1 0 0
182 1 0 0 0 0 0 1 0 0
224 1 0 0 0 0 0 1 0 0
236 2 1 1 0 0 0 2 0 0
238 5 0 0 0 0 0 1 0 0
250 3 0 0 1 0 0 0 0 0
253 5 1 1 1 0 0 1 0 0
254 1 1 0 1 1 0 0 0 0
255 8 0 0 7 1 0 0 0 0
fn=_dl_sysdep_start_cleanup
260 1 1 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../elf/dl-tls.c
fn=_dl_add_to_slotinfo
887 4 1 1 0 0 0 3 0 0
893 2 0 0 1 0 0 0 0 0
896 1 0 0 1 1 0 0 0 0
901 7 1 1 2 1 0 0 0 0
942 1 0 0 0 0 0 1 0 0
943 1 0 0 0 0 0 1 0 0
944 4 0 0 4 0 0 0 0 0
fn=_dl_allocate_tls_init
437 9 1 1 0 0 0 7 0 0
438 2 0 0 0 0 0 0 0 0
442 2 0 0 1 0 0 1 0 0
444 2 0 0 0 0 0 0 0 0
445 1 1 1 0 0 0 0 0 0
448 3 0 0 2 1 0 0 0 0
460 2 0 0 1 0 0 1 0 0
465 11 0 0 2 0 0 1 0 0
471 15 1 1 0 0 0 1 0 0
474 1 0 0 1 0 0 0 0 0
475 2 0 0 0 0 0 0 0 0
481 3 1 1 2 0 0 0 0 0
482 2 0 0 0 0 0 0 0 0
484 6 0 0 2 0 0 1 1 1
485 1 1 1 0 0 0 1 0 0
487 2 0 0 0 0 0 0 0 0
488 2 0 0 1 0 0 0 0 0
491 2 0 0 0 0 0 0 0 0
492 4 0 0 2 0 0 0 0 0
494 2 0 0 0 0 0 0 0 0
495 2 0 0 1 0 0 0 0 0
504 1 0 0 0 0 0 1 0 0
507 15 1 1 6 0 0 2 0 0
517 1 1 1 0 0 0 0 0 0
521 3 0 0 2 0 0 1 0 0
524 8 0 0 7 0 0 0 0 0
fn=_dl_allocate_tls_storage
285 2 0 0 1 0 0 0 0 0
286 3 0 0 0 0 0 1 0 0
287 2 1 1 0 0 0 0 0 0
290 1 0 0 0 0 0 1 0 0
296 2 0 0 0 0 0 1 0 0
332 3 1 1 0 0 0 3 0 0
334 1 0 0 1 0 0 0 0 0
345 1 1 1 1 0 0 0 0 0
346 2 0 0 0 0 0 1 0 0
347 3 0 0 0 0 0 0 0 0
355 4 0 0 0 0 0 0 0 0
356 1 0 0 0 0 0 0 0 0
360 297 1 1 0 0 0 289 36 36
379 1 0 0 0 0 0 1 1 1
385 5 0 0 4 0 0 0 0 0
fn=_dl_count_modids
113 2 1 1 1 0 0 0 0 0
114 2 0 0 2 1 1 0 0 0
fn=_dl_determine_tlsoffset
135 5 0 0 0 0 0 5 0 0
136 2 0 0 0 0 0 0 0 0
137 1 0 0 0 0 0 0 0 0
138 1 0 0 0 0 0 0 0 0
141 3 1 1 1 0 0 0 0 0
144 2 0 0 1 0 0 0 0 0
178 1 0 0 0 0 0 0 0 0
180 13 1 1 2 0 0 0 0 0
182 4 1 1 1 0 0 0 0 0
184 3 1 1 1 0 0 0 0 0
185 2 1 1 1 0 0 0 0 0
187 2 0 0 0 0 0 0 0 0
189 5 0 0 1 0 0 0 0 0
205 8 0 0 0 0 0 0 0 0
207 2 0 0 0 0 0 0 0 0
208 2 0 0 0 0 0 0 0 0
217 1 0 0 0 0 0 1 0 0
220 1 0 0 0 0 0 1 0 0
221 1 1 1 0 0 0 1 0 0
272 1 0 0 0 0 0 1 0 0
273 6 0 0 6 0 0 0 0 0
fn=_dl_next_tls_modid
51 4 1 1 2 0 0 0 0 0
99 1 0 0 0 0 0 1 0 0
103 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../misc/sbrk.c
fn=sbrk
32 4 0 0 0 0 0 2 0 0
40 6 1 1 2 0 0 0 0 0
44 2 0 0 0 0 0 0 0 0
60 5 1 1 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/generic/ldsodefs.h
fn=_dl_relocate_object
102 273 0 0 91 0 0 0 0 0
fn=do_lookup_x
102 246 1 1 82 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/posix/dl-fileid.h
fn=_dl_map_object_from_fd
37 12 1 1 0 0 0 2 0 0
40 2 0 0 2 0 0 0 0 0
41 4 0 0 2 0 0 2 0 0
49 13 0 0 7 1 1 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/dl-osinfo.h
fn=dl_main
64 2 0 0 1 0 0 0 0 0
77 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/dl-sysdep.c
fn=_dl_discover_osversion
45 4 1 1 0 0 0 3 0 0
47 3 1 1 1 0 0 0 0 0
87 5 1 1 0 0 0 1 1 1
102 1 0 0 0 0 0 0 0 0
106 1 0 0 0 0 0 0 0 0
107 1 0 0 0 0 0 0 0 0
109 12 0 0 3 1 1 0 0 0
111 6 0 0 0 0 0 0 0 0
113 17 1 1 4 0 0 0 0 0
115 1 0 0 0 0 0 0 0 0
116 2 0 0 0 0 0 0 0 0
119 3 0 0 0 0 0 0 0 0
120 3 0 0 0 0 0 0 0 0
121 3 0 0 0 0 0 0 0 0
123 13 0 0 0 0 0 0 0 0
128 2 1 1 0 0 0 0 0 0
132 5 1 1 4 0 0 0 0 0
fn=_dl_sysdep_start
35 2 0 0 0 0 0 1 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/dl-vdso.c
fn=_dl_vdso_vsym
25 20 1 1 4 1 0 4 0 0
26 8 0 0 8 1 0 0 0 0
27 4 1 1 0 0 0 0 0 0
30 8 0 0 0 0 0 0 0 0
47 4 0 0 0 0 0 0 0 0
48 24 1 1 12 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/not-errno.h
fn=_dl_important_hwcaps
28 4 1 1 0 0 0 0 0 0
fn=_dl_load_cache_lookup
28 4 0 0 0 0 0 0 0 0
32 3 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/unix/sysv/linux/x86_64/brk.c
fn=brk
31 7 1 1 0 0 0 1 1 1
33 2 1 1 0 0 0 0 0 0
39 1 0 0 0 0 0 0 0 0
40 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86/cpu-features.c
fn=_dl_sysdep_start
37 2 0 0 0 0 0 0 0 0
38 2 0 0 0 0 0 0 0 0
39 6 1 1 0 0 0 4 0 0
198 1 0 0 0 0 0 1 0 0
199 1 1 1 0 0 0 1 0 0
210 3 0 0 0 0 0 1 0 0
213 6 0 0 0 0 0 0 0 0
217 3 0 0 0 0 0 1 0 0
219 6 1 1 0 0 0 1 0 0
224 4 0 0 2 0 0 0 0 0
226 3 1 1 2 0 0 1 0 0
227 7 0 0 1 1 1 0 0 0
273 3 0 0 2 0 0 0 0 0
295 2 0 0 1 0 0 0 0 0
305 7 2 2 0 0 0 1 0 0
318 3 0 0 0 0 0 1 0 0
327 4 0 0 0 0 0 0 0 0
334 6 0 0 1 0 0 0 0 0
381 3 1 1 1 0 0 0 0 0
382 1 0 0 1 0 0 0 0 0
385 2 0 0 0 0 0 0 0 0
386 1 0 0 1 0 0 0 0 0
392 1 0 0 0 0 0 1 0 0
393 1 0 0 0 0 0 1 0 0
394 1 0 0 0 0 0 1 0 0
397 4 1 1 0 0 0 1 0 0
399 6 0 0 1 0 0 2 0 0
401 6 1 1 1 0 0 2 0 0
403 6 0 0 1 0 0 2 0 0
414 1 0 0 0 0 0 1 0 0
415 2 0 0 1 0 0 0 0 0
419 3 1 1 1 0 0 0 0 0
438 3 1 1 0 0 0 0 0 0
440 4 1 1 1 0 0 0 0 0
441 2 0 0 1 0 0 0 0 0
443 4 0 0 1 0 0 0 0 0
444 2 1 1 0 0 0 0 0 0
447 2 0 0 0 0 0 1 0 0
fn=get_common_indeces.constprop.1
48 2 1 1 0 0 0 1 0 0
52 4 0 0 0 0 0 0 0 0
55 5 0 0 0 0 0 3 0 0
58 1 0 0 0 0 0 1 0 0
59 4 1 1 0 0 0 1 0 0
60 4 0 0 0 0 0 1 0 0
61 4 0 0 0 0 0 1 0 0
62 3 0 0 0 0 0 1 0 0
63 2 1 1 1 0 0 0 0 0
70 2 0 0 1 0 0 0 0 0
71 7 0 0 0 0 0 4 0 0
78 3 1 1 1 0 0 0 0 0
82 2 0 0 0 0 0 0 0 0
84 4 0 0 0 0 0 0 0 0
88 2 1 1 0 0 0 0 0 0
91 4 0 0 1 1 1 1 0 0
94 2 0 0 1 0 0 0 0 0
96 3 0 0 0 0 0 1 0 0
98 2 0 0 0 0 0 0 0 0
100 3 0 0 0 0 0 1 0 0
105 3 1 1 0 0 0 0 0 0
124 2 0 0 1 0 0 0 0 0
128 4 0 0 0 0 0 0 0 0
129 2 0 0 0 0 0 0 0 0
131 1 0 0 0 0 0 0 0 0
132 1 0 0 0 0 0 0 0 0
135 2 1 1 0 0 0 1 0 0
137 1 0 0 0 0 0 1 0 0
139 3 0 0 0 0 0 0 0 0
142 2 0 0 0 0 0 0 0 0
192 3 1 1 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86/dl-hwcap.h
fn=_dl_important_hwcaps
57 6 0 0 0 0 0 2 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86/dl-procinfo.h
fn=_dl_load_cache_lookup
39 4 0 0 0 0 0 1 0 0
42 8 1 1 0 0 0 2 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86_64/dl-machine.h
fn=_dl_fixup
242 2 0 0 0 0 0 2 0 0
fn=_dl_relocate_object
76 16 1 1 4 0 0 0 0 0
82 4 1 1 4 1 0 0 0 0
86 6 0 0 2 2 1 0 0 0
92 2 1 1 0 0 0 2 0 0
100 6 0 0 2 0 0 0 0 0
120 4 0 0 2 0 0 0 0 0
122 4 0 0 0 0 0 2 0 0
124 8 0 0 2 0 0 0 0 0
131 6 1 1 2 1 0 0 0 0
276 216 0 0 0 0 0 0 0 0
297 216 0 0 0 0 0 0 0 0
301 216 0 0 0 0 0 0 0 0
308 4442 12 12 830 83 70 624 4 0
310 473 1 1 200 0 0 0 0 0
313 400 3 3 100 0 0 0 0 0
335 648 0 0 108 3 3 0 0 0
430 51 1 1 17 0 0 0 0 0
434 68 1 1 17 1 0 0 0 0
439 51 0 0 34 2 2 0 0 0
448 51 0 0 17 0 0 17 8 8
458 364 2 2 182 11 10 91 10 6
481 12 0 0 0 0 0 4 0 0
491 6 0 0 0 0 0 3 1 0
535 3732 0 0 1244 312 311 0 0 0
540 2488 1 1 0 0 0 0 0 0
541 3732 0 0 1244 156 156 1244 237 234
551 94 0 0 47 0 0 0 0 0
555 16 0 0 0 0 0 0 0 0
557 24 0 0 8 1 0 0 0 0
558 8 0 0 8 5 4 0 0 0
575 78 0 0 78 1 1 0 0 0
577 39 0 0 0 0 0 39 0 0
578 39 0 0 0 0 0 39 2 2
fn=_dl_start
59 3 0 0 1 1 1 0 0 0
301 27 0 0 0 0 0 0 0 0
310 45 0 0 18 1 1 0 0 0
313 36 0 0 9 7 7 0 0 0
335 55 0 0 9 1 1 0 0 0
354 27 1 1 9 1 1 9 2 2
422 1 0 0 0 0 0 0 0 0
540 78 0 0 39 5 5 0 0 0
541 117 1 1 39 5 5 39 21 21
fl=/build/glibc-S9d2JN/glibc-2.27/elf/../sysdeps/x86_64/dl-trampoline.h
fn=_dl_runtime_resolve_xsave
71 2 1 1 0 0 0 2 0 0
74 2 0 0 0 0 0 0 0 0
76 2 0 0 0 0 0 0 0 0
86 2 0 0 2 1 0 0 0 0
92 2 0 0 0 0 0 2 2 1
93 2 0 0 0 0 0 2 0 0
94 2 0 0 0 0 0 2 0 0
95 2 1 1 0 0 0 2 0 0
96 2 0 0 0 0 0 2 0 0
97 2 0 0 0 0 0 2 0 0
98 2 0 0 0 0 0 2 0 0
102 2 0 0 0 0 0 0 0 0
103 2 0 0 0 0 0 0 0 0
106 2 0 0 0 0 0 2 2 0
107 2 0 0 0 0 0 2 0 0
109 2 0 0 0 0 0 2 0 0
110 2 0 0 0 0 0 2 0 0
111 2 0 0 0 0 0 2 0 0
112 2 1 1 0 0 0 2 0 0
113 2 0 0 0 0 0 2 0 0
114 2 0 0 0 0 0 2 0 0
116 2 0 0 2 0 0 66 19 2
123 2 0 0 2 0 0 0 0 0
124 2 0 0 2 0 0 0 0 0
125 2 0 0 0 0 0 2 2 1
126 2 0 0 0 0 0 0 0 0
131 2 0 0 0 0 0 0 0 0
132 2 0 0 0 0 0 0 0 0
133 2 0 0 72 0 0 0 0 0
135 2 0 0 2 0 0 0 0 0
136 2 1 1 2 0 0 0 0 0
137 2 0 0 2 0 0 0 0 0
138 2 0 0 2 0 0 0 0 0
139 2 0 0 2 0 0 0 0 0
140 2 0 0 2 0 0 0 0 0
141 2 0 0 2 0 0 0 0 0
143 2 0 0 0 0 0 0 0 0
145 2 0 0 2 0 0 0 0 0
149 2 0 0 0 0 0 0 0 0
152 2 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/./dl-load.h
fn=_dl_map_object_from_fd
90 8 0 0 4 0 0 0 0 0
91 6 0 0 4 0 0 2 0 0
93 8 0 0 4 0 0 0 0 0
94 5 0 0 3 0 0 0 0 0
95 6 1 1 2 0 0 0 0 0
96 4 0 0 1 0 0 0 0 0
98 4 0 0 0 0 0 1 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/./dl-map-segments.h
fn=_dl_map_object_from_fd
50 4 1 1 2 0 0 0 0 0
56 14 0 0 6 0 0 6 0 0
60 6 0 0 2 0 0 0 0 0
63 6 0 0 2 0 0 2 0 0
64 4 1 1 0 0 0 2 0 0
66 4 0 0 2 0 0 0 0 0
73 26 2 2 8 0 0 4 0 0
80 4 0 0 2 0 0 0 0 0
90 20 0 0 0 0 0 0 0 0
92 12 0 0 6 0 0 2 0 0
94 24 1 1 8 0 0 4 0 0
104 16 1 1 8 0 0 0 0 0
110 4 1 1 2 0 0 0 0 0
111 2 0 0 0 0 0 0 0 0
112 10 0 0 2 0 0 0 0 0
113 4 0 0 0 0 0 0 0 0
120 6 0 0 0 0 0 0 0 0
123 4 1 1 2 0 0 0 0 0
131 20 0 0 6 0 0 8 0 0
137 4 1 1 0 0 0 0 0 0
141 9 0 0 1 0 0 2 0 0
144 3 0 0 1 0 0 0 0 0
149 4 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-addr.c
fn=_dl_addr
30 2 0 0 1 0 0 1 0 0
31 2 0 0 1 0 0 1 0 0
34 2 0 0 1 0 0 0 0 0
38 1 0 0 1 0 0 0 0 0
39 1 0 0 1 0 0 0 0 0
40 3 1 1 2 0 0 1 0 0
42 3 0 0 2 0 0 1 0 0
44 2 0 0 0 0 0 0 0 0
45 2 0 0 1 1 0 0 0 0
50 4050 0 0 2 0 0 0 0 0
52 1011 1 1 1011 60 21 0 0 0
53 2022 0 0 0 0 0 0 0 0
55 3664 0 0 916 0 0 0 0 0
61 11625 1 1 2325 482 454 0 0 0
63 9300 0 0 2325 0 0 0 0 0
64 16858 1 1 5300 378 344 0 0 0
69 2325 0 0 0 0 0 0 0 0
71 8384 0 0 2325 140 90 0 0 0
100 2 1 1 0 0 0 0 0 0
101 1 0 0 0 0 0 1 1 0
102 3 0 0 1 1 0 0 0 0
105 2 0 0 0 0 0 0 0 0
117 1 1 1 0 0 0 1 1 0
118 1 0 0 0 0 0 1 0 0
126 11 1 1 0 0 0 7 2 0
128 1 0 0 0 0 0 0 0 0
131 3 0 0 2 1 0 1 0 0
133 2 0 0 0 0 0 1 0 0
135 3 1 1 0 0 0 0 0 0
138 2 0 0 0 0 0 0 0 0
141 2 0 0 1 1 0 1 0 0
144 9 0 0 7 1 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-cache.c
fn=_dl_cache_libcmp
141 22 1 1 22 10 10 0 0 0
142 134 0 0 0 0 0 0 0 0
144 256 0 0 0 0 0 0 0 0
146 6 0 0 0 0 0 0 0 0
152 12 0 0 0 0 0 0 0 0
153 9 0 0 0 0 0 0 0 0
154 12 1 1 3 0 0 0 0 0
156 12 0 0 3 0 0 0 0 0
158 6 0 0 0 0 0 0 0 0
164 122 0 0 0 0 0 0 0 0
166 228 0 0 106 0 0 0 0 0
167 24 1 1 8 0 0 0 0 0
170 53 1 1 0 0 0 0 0 0
171 53 0 0 0 0 0 0 0 0
174 9 0 0 3 0 0 0 0 0
fn=_dl_load_cache_lookup
187 9 1 1 0 0 0 6 0 0
195 2 0 0 1 0 0 0 0 0
198 3 0 0 1 1 1 0 0 0
201 5 1 1 0 0 0 1 1 1
209 5 0 0 1 0 0 0 0 0
210 7 1 1 3 1 1 0 0 0
214 1 0 0 0 0 0 1 0 0
217 4 0 0 1 0 0 0 0 0
220 2 1 1 0 0 0 1 0 0
221 3 0 0 0 0 0 0 0 0
222 8 0 0 3 2 2 0 0 0
243 1 1 1 0 0 0 0 0 0
249 2 0 0 0 0 0 0 0 0
258 3 0 0 0 0 0 1 0 0
260 1 0 0 1 0 0 0 0 0
264 6 1 1 1 0 0 2 0 0
266 2 0 0 0 0 0 0 0 0
270 7 0 0 3 0 0 3 0 0
271 3 0 0 1 0 0 0 0 0
285 251 9 9 35 9 9 21 0 0
297 10 2 2 2 0 0 0 0 0
301 2 0 0 1 0 0 0 0 0
305 2 0 0 1 0 0 0 0 0
313 9 1 1 1 0 0 1 0 0
314 3 0 0 0 0 0 1 0 0
315 2 0 0 0 0 0 1 0 0
316 8 0 0 7 0 0 0 0 0
fn=_dl_unload_cache
325 1 0 0 0 0 0 0 0 0
326 4 1 1 1 1 0 0 0 0
328 2 0 0 1 0 0 1 0 0
329 1 1 1 0 0 0 1 0 0
331 2 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-debug.c
fn=_dl_debug_initialize
49 8 2 1 0 0 0 0 0 0
50 4 1 1 4 0 0 0 0 0
54 14 0 0 4 0 0 0 0 0
57 1 0 0 0 0 0 1 0 0
58 6 2 1 3 0 0 1 0 0
59 5 0 0 1 0 0 1 0 0
60 2 0 0 0 0 0 1 0 0
64 1 0 0 1 0 0 0 0 0
fn=_dl_debug_state
74 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-deps.c
fn=_dl_map_object_deps
143 4 0 0 0 0 0 2 0 0
144 2 0 0 0 0 0 2 0 0
145 7 0 0 0 0 0 2 0 0
147 2 0 0 0 0 0 0 0 0
151 9 1 1 2 0 0 3 0 0
158 11 0 0 0 0 0 9 0 0
159 9 2 2 0 0 0 0 0 0
175 10 1 1 1 0 0 2 0 0
176 1 0 0 1 0 0 0 0 0
179 1 0 0 0 0 0 1 0 0
185 1 0 0 0 0 0 1 0 0
186 1 0 0 0 0 0 1 0 0
198 2 0 0 1 0 0 1 0 0
199 2 0 0 0 0 0 0 0 0
200 2 1 1 0 0 0 2 0 0
206 6 1 1 0 0 0 4 0 0
209 4 0 0 0 0 0 4 0 0
213 12 1 1 4 0 0 0 0 0
214 25 2 2 11 0 0 0 0 0
216 2 0 0 0 0 0 0 0 0
218 8 0 0 4 0 0 0 0 0
220 26 0 0 0 0 0 4 0 0
225 16 1 1 8 1 1 0 0 0
227 6 0 0 4 0 0 2 0 0
232 2 0 0 0 0 0 2 0 0
233 2 0 0 0 0 0 2 0 0
234 4 1 1 2 0 0 2 0 0
235 4 0 0 2 0 0 2 0 0
238 216 0 0 57 0 0 2 0 0
239 102 1 1 0 0 0 0 0 0
245 18 0 0 4 0 0 2 0 0
247 2 0 0 0 0 0 2 0 0
249 8 1 1 4 0 0 2 0 0
250 4 1 1 2 0 0 0 0 0
259 2 0 0 2 0 0 0 0 0
261 4 0 0 2 0 0 0 0 0
266 6 0 0 0 0 0 0 0 0
269 2 0 0 0 0 0 2 0 0
270 2 0 0 0 0 0 2 0 0
271 2 0 0 0 0 0 2 0 0
272 4 1 1 2 0 0 2 0 0
274 2 0 0 2 0 0 0 0 0
276 10 0 0 2 0 0 4 0 0
280 4 0 0 0 0 0 0 0 0
281 4 0 0 1 0 0 2 0 0
283 147 1 1 0 0 0 0 0 0
304 10 1 1 0 0 0 4 0 0
434 8 1 1 0 0 0 0 0 0
436 6 1 1 2 0 0 2 0 0
438 4 0 0 0 0 0 2 0 0
439 4 0 0 0 0 0 0 0 0
440 4 0 0 0 0 0 0 0 0
443 2 0 0 0 0 0 2 1 1
444 10 0 0 0 0 0 2 0 0
445 12 0 0 2 0 0 2 0 0
448 2 0 0 0 0 0 2 0 0
449 2 0 0 2 0 0 0 0 0
453 22 1 1 11 0 0 0 0 0
455 4 1 1 4 0 0 0 0 0
456 18 1 1 4 0 0 0 0 0
460 6 1 1 2 0 0 0 0 0
461 2 0 0 0 0 0 1 0 0
464 5 0 0 2 0 0 1 0 0
474 2 1 1 0 0 0 2 0 0
475 4 1 1 1 0 0 1 0 0
477 3 0 0 1 0 0 0 0 0
482 7 0 0 3 0 0 1 0 0
483 1 0 0 0 0 0 1 0 0
485 20 1 1 8 0 0 0 0 0
491 8 0 0 0 0 0 4 1 1
495 12 0 0 8 0 0 0 0 0
498 2 0 0 1 0 0 0 0 0
549 3 1 1 2 0 0 0 0 0
550 1 0 0 0 0 0 0 0 0
551 3 0 0 1 0 0 0 0 0
573 6 1 1 0 0 0 3 0 0
586 7 2 2 1 0 0 2 0 0
590 5 0 0 0 0 0 1 0 0
593 1 0 0 0 0 0 1 0 0
595 2 0 0 1 0 0 1 0 0
596 1 0 0 1 0 0 0 0 0
597 3 1 1 1 0 0 0 0 0
604 3 0 0 1 0 0 0 0 0
607 2 1 1 0 0 0 0 0 0
610 8 0 0 7 0 0 0 0 0
fn=openaux
60 4 1 1 0 0 0 2 0 0
63 20 1 1 8 0 0 4 0 0
64 4 0 0 2 0 0 0 0 0
67 2 0 0 2 0 0 0 0 0
68 4 0 0 4 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-environ.c
fn=_dl_next_ld_env_entry
29 5 1 1 5 0 0 0 0 0
32 184 0 0 61 0 0 0 0 0
34 120 0 0 60 0 0 0 0 0
35 44 0 0 22 0 0 0 0 0
37 4 0 0 0 0 0 0 0 0
40 8 1 1 0 0 0 4 0 0
42 4 0 0 4 0 0 0 0 0
45 56 0 0 0 0 0 0 0 0
49 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-error-skeleton.c
fn=_dl_catch_error
213 7 1 1 0 0 0 3 0 0
215 4 0 0 0 0 0 1 0 0
216 2 1 1 1 0 0 1 0 0
217 2 0 0 1 0 0 1 0 0
218 2 0 0 1 0 0 1 0 0
220 5 0 0 4 0 0 0 0 0
fn=_dl_catch_exception
175 12 1 1 0 0 0 9 0 0
187 6 1 1 0 0 0 6 3 3
188 6 0 0 0 0 0 3 0 0
190 6 0 0 3 0 0 3 0 0
191 6 0 0 0 0 0 3 0 0
194 18 0 0 0 0 0 3 0 0
196 9 1 1 6 0 0 3 0 0
197 6 0 0 3 0 0 3 0 0
198 12 0 0 3 0 0 6 0 0
207 12 0 0 6 0 0 0 0 0
fn=_dl_receive_error
226 3 0 0 0 0 0 2 0 0
227 1 0 0 1 0 0 0 0 0
228 1 1 1 1 0 0 0 0 0
231 1 0 0 0 0 0 1 0 0
232 1 0 0 0 0 0 1 0 0
234 2 0 0 0 0 0 1 0 0
236 1 0 0 0 0 0 1 0 0
237 1 0 0 0 0 0 1 0 0
238 4 0 0 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-fini.c
fn=_dl_fini
30 8 1 1 0 0 0 6 0 0
47 6 0 0 0 0 0 1 0 0
50 7 0 0 1 0 0 0 0 0
53 2 1 1 1 0 0 1 0 0
55 1 0 0 1 1 0 0 0 0
58 2 0 0 0 0 0 0 0 0
60 8 1 1 3 0 0 1 0 0
65 1 0 0 0 0 0 1 0 0
68 7 0 0 0 0 0 0 0 0
73 13 0 0 4 0 0 0 0 0
75 8 1 1 4 0 0 0 0 0
77 8 0 0 0 0 0 0 0 0
79 8 0 0 0 0 0 4 0 0
80 4 0 0 0 0 0 4 4 0
81 4 0 0 0 0 0 0 0 0
85 4 0 0 4 0 0 0 0 0
87 6 1 1 0 0 0 0 0 0
88 4 0 0 0 0 0 0 0 0
94 10 1 1 0 0 0 1 0 0
104 2 1 1 1 0 0 1 0 0
109 16 0 0 5 0 0 1 0 0
111 4 0 0 4 0 0 0 0 0
113 12 0 0 4 0 0 0 0 0
116 8 0 0 0 0 0 4 0 0
119 12 1 1 4 4 0 0 0 0
120 6 1 1 2 2 0 0 0 0
123 4 0 0 2 0 0 0 0 0
134 6 0 0 4 2 0 0 0 0
135 2 0 0 2 0 0 0 0 0
136 4 0 0 2 0 0 0 0 0
137 20 1 1 4 1 0 2 0 0
138 4 0 0 2 2 0 2 0 0
142 4 0 0 0 0 0 0 0 0
143 6 0 0 4 0 0 2 0 0
149 24 1 1 8 1 0 0 0 0
165 8 0 0 4 0 0 0 0 0
171 6 0 0 2 0 0 0 0 0
177 2 0 0 1 0 0 0 0 0
184 8 0 0 7 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-hwcaps.c
fn=_dl_important_hwcaps
42 13 2 2 0 0 0 10 1 1
43 8 0 0 1 0 0 3 1 1
46 3 0 0 0 0 0 0 0 0
55 18 1 1 1 0 0 0 0 0
56 6 0 0 0 0 0 0 0 0
57 4 0 0 0 0 0 0 0 0
65 3 1 1 1 0 0 0 0 0
69 3 1 1 0 0 0 0 0 0
129 1 0 0 0 0 0 0 0 0
131 4 1 1 0 0 0 0 0 0
146 7 0 0 0 0 0 0 0 0
147 1 0 0 0 0 0 0 0 0
149 2 0 0 0 0 0 0 0 0
166 1 0 0 0 0 0 0 0 0
183 19 2 2 2 0 0 1 0 0
184 6 0 0 2 0 0 2 1 1
186 1 0 0 0 0 0 1 0 0
187 2 0 0 0 0 0 2 1 1
188 7 0 0 1 0 0 0 0 0
191 3 1 1 1 0 0 0 0 0
193 1 0 0 0 0 0 1 0 0
194 6 0 0 1 0 0 1 0 0
198 2 0 0 0 0 0 1 0 0
199 1 0 0 0 0 0 1 0 0
202 3 0 0 1 0 0 0 0 0
205 4 1 1 0 0 0 1 0 0
209 8 0 0 1 0 0 2 0 0
210 4 0 0 1 0 0 0 0 0
212 3 1 1 0 0 0 0 0 0
213 2 0 0 0 0 0 0 0 0
214 3 0 0 1 0 0 0 0 0
215 2 0 0 0 0 0 0 0 0
222 2 1 1 0 0 0 0 0 0
228 11 0 0 1 0 0 5 0 0
229 5 1 1 0 0 0 1 0 0
230 4 0 0 2 0 0 0 0 0
259 10 0 0 0 0 0 3 0 0
262 6 1 1 2 0 0 2 0 0
265 2 1 1 0 0 0 0 0 0
269 1 0 0 1 0 0 0 0 0
272 2 0 0 0 0 0 0 0 0
275 12 0 0 4 0 0 4 0 0
278 13 1 1 3 0 0 0 0 0
279 24 1 1 1 0 0 6 0 0
280 6 0 0 2 0 0 2 0 0
283 10 1 1 4 0 0 4 0 0
285 7 0 0 3 0 0 0 0 0
290 28 1 1 2 0 0 0 0 0
291 16 0 0 0 0 0 8 1 1
295 22 1 1 0 0 0 0 0 0
298 51 0 0 0 0 0 0 0 0
299 72 0 0 0 0 0 0 0 0
300 36 0 0 24 0 0 0 0 0
302 6 0 0 0 0 0 0 0 0
305 3 0 0 1 0 0 0 0 0
306 2 0 0 0 0 0 0 0 0
307 15 1 1 1 0 0 0 0 0
309 6 0 0 0 0 0 0 0 0
310 2 1 1 2 0 0 0 0 0
313 4 0 0 0 0 0 2 0 0
320 19 0 0 6 0 0 4 0 0
321 4 0 0 0 0 0 0 0 0
323 8 0 0 0 0 0 0 0 0
326 3 0 0 2 0 0 1 0 0
328 2 1 1 1 0 0 0 0 0
329 9 1 1 7 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-init.c
fn=_dl_init
30 15 2 2 5 0 0 0 0 0
36 8 0 0 0 0 0 4 0 0
39 16 0 0 8 1 0 0 0 0
40 3 1 1 0 0 0 0 0 0
44 9 1 1 3 2 0 0 0 0
45 3 1 1 1 0 0 0 0 0
49 4 0 0 2 0 0 0 0 0
58 15 1 1 6 2 0 3 0 0
61 1 0 0 1 0 0 0 0 0
62 4 0 0 0 0 0 0 0 0
68 6 1 1 4 1 0 0 0 0
70 5 0 0 4 0 0 0 0 0
71 23 1 1 4 0 0 3 0 0
72 14 1 1 3 0 0 3 0 0
79 11 1 1 0 0 0 6 0 0
80 1 0 0 1 1 0 0 0 0
81 1 0 0 1 0 0 0 0 0
84 3 1 1 1 0 0 0 0 0
87 2 0 0 0 0 0 1 0 0
92 2 0 0 0 0 0 0 0 0
117 2 0 0 1 0 0 0 0 0
118 15 0 0 0 0 0 0 0 0
119 12 0 0 8 0 0 0 0 0
125 8 0 0 7 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-load.c
fn=_dl_dst_count
230 14 1 1 0 0 0 12 1 1
233 4 0 0 0 0 0 2 0 0
236 4 0 0 0 0 0 0 0 0
237 2 0 0 0 0 0 0 0 0
256 18 1 1 14 0 0 0 0 0
fn=_dl_init_paths
678 9 2 2 0 0 0 7 0 0
691 6 0 0 2 0 0 2 1 1
695 1 1 1 0 0 0 1 0 0
696 2 0 0 0 0 0 1 0 0
697 3 0 0 0 0 0 0 0 0
704 4 0 0 0 0 0 0 0 0
705 5 0 0 1 0 0 2 0 0
708 6 1 1 0 0 0 2 0 0
710 2 0 0 0 0 0 0 0 0
716 1 0 0 0 0 0 1 0 0
717 1 0 0 0 0 0 1 0 0
719 1 0 0 0 0 0 0 0 0
725 3 0 0 0 0 0 3 0 0
727 8 0 0 0 0 0 4 0 0
728 4 0 0 0 0 0 4 3 3
730 5 0 0 0 0 0 4 0 0
731 8 1 1 3 0 0 4 1 1
732 7 1 1 0 0 0 0 0 0
735 6 0 0 3 2 2 0 0 0
736 24 0 0 8 0 0 4 0 0
739 30 1 1 3 0 0 5 0 0
745 1 0 0 0 0 0 1 1 1
746 1 1 1 0 0 0 1 0 0
750 1 0 0 1 0 0 0 0 0
751 2 0 0 0 0 0 0 0 0
753 4 0 0 1 0 0 0 0 0
755 3 0 0 1 0 0 0 0 0
772 2 0 0 0 0 0 1 0 0
774 3 1 1 1 0 0 0 0 0
788 2 1 1 0 0 0 1 0 0
793 5 1 1 2 0 0 0 0 0
795 12 2 2 0 0 0 2 0 0
799 2 0 0 0 0 0 0 0 0
800 61 1 1 15 0 0 0 0 0
801 56 0 0 0 0 0 0 0 0
804 1 0 0 0 0 0 1 0 0
805 1 0 0 0 0 0 1 0 0
806 2 0 0 0 0 0 0 0 0
812 7 0 0 0 0 0 1 0 0
815 3 0 0 2 0 0 0 0 0
821 1 0 0 0 0 0 1 0 0
825 8 0 0 7 0 0 0 0 0
fn=_dl_map_object
656 9 1 1 3 0 0 0 0 0
665 3 1 1 2 0 0 0 0 0
2151 27 2 2 0 0 0 24 4 4
2153 2 0 0 0 0 0 2 0 0
2159 6 0 0 0 0 0 0 0 0
2160 12 0 0 3 1 1 0 0 0
2163 42 1 1 9 0 0 0 0 0
2168 49 0 0 7 0 0 0 0 0
2170 35 1 1 0 0 0 7 0 0
2174 12 0 0 6 0 0 0 0 0
2175 18 0 0 6 0 0 0 0 0
2178 2 0 0 2 0 0 0 0 0
2179 4 0 0 4 0 0 0 0 0
2180 8 0 0 0 0 0 2 0 0
2196 6 1 1 2 0 0 0 0 0
2206 6 0 0 2 0 0 0 0 0
2240 2 0 0 0 0 0 2 2 2
2242 11 2 2 1 0 0 2 0 0
2246 4 0 0 0 0 0 2 0 0
2248 2 0 0 0 0 0 0 0 0
2255 4 0 0 1 0 0 0 0 0
2259 4 2 2 1 0 0 1 0 0
2260 2 0 0 0 0 0 1 0 0
2264 3 0 0 1 0 0 0 0 0
2267 7 0 0 0 0 0 3 0 0
2279 3 0 0 0 0 0 0 0 0
2280 7 1 1 1 0 0 1 0 0
2290 2 1 1 1 0 0 0 0 0
2291 15 2 2 1 0 0 4 0 0
2297 5 0 0 0 0 0 0 0 0
2306 1 0 0 0 0 0 1 1 1
2320 2 1 1 0 0 0 0 0 0
2322 3 0 0 1 0 0 0 0 0
2326 3 0 0 0 0 0 1 0 0
2328 2 0 0 0 0 0 0 0 0
2332 2 1 1 0 0 0 0 0 0
2340 3 0 0 1 0 0 0 0 0
2363 11 0 0 0 0 0 3 0 0
2367 5 1 1 3 0 0 0 0 0
2368 2 0 0 0 0 0 1 0 0
2385 2 1 1 1 0 0 0 0 0
2391 1 0 0 0 0 0 1 1 1
2393 6 0 0 0 0 0 1 0 0
2394 5 0 0 0 0 0 1 0 0
2398 10 1 1 0 0 0 2 0 0
2401 5 0 0 3 0 0 0 0 0
2413 7 1 1 0 0 0 0 0 0
2415 2 0 0 0 0 0 0 0 0
2459 4 0 0 2 0 0 2 0 0
2460 30 1 1 6 0 0 10 0 0
2462 27 1 1 21 0 0 0 0 0
fn=_dl_map_object_from_fd
424 2 1 1 1 0 0 0 0 0
863 30 1 1 0 0 0 22 2 2
873 8 1 1 2 0 0 4 1 1
874 2 0 0 0 0 0 2 0 0
889 29 0 0 9 0 0 0 0 0
890 10 1 1 5 0 0 0 0 0
907 4 1 1 2 0 0 0 0 0
931 8 0 0 2 0 0 2 0 0
941 4 1 1 2 0 0 0 0 0
963 8 0 0 4 0 0 0 0 0
995 4 0 0 0 0 0 0 0 0
998 16 1 1 10 0 0 2 0 0
999 4 0 0 0 0 0 0 0 0
1010 6 0 0 4 0 0 2 2 2
1011 8 0 0 4 0 0 4 0 0
1012 4 0 0 2 0 0 2 0 0
1014 6 1 1 0 0 0 0 0 0
1015 8 0 0 4 0 0 0 0 0
1016 2 0 0 0 0 0 0 0 0
1031 6 0 0 0 0 0 4 0 0
1033 2 0 0 0 0 0 2 0 0
1035 20 1 1 2 0 0 2 0 0
1036 2 0 0 0 0 0 0 0 0
1037 2 1 1 0 0 0 2 0 0
1043 112 0 0 0 0 0 0 0 0
1044 127 2 2 17 2 2 0 0 0
1050 4 0 0 2 0 0 0 0 0
1055 4 0 0 2 0 0 2 0 0
1056 8 0 0 2 0 0 2 0 0
1061 2 1 1 1 0 0 1 0 0
1062 1 0 0 0 0 0 0 0 0
1067 20 2 2 8 0 0 0 0 0
1072 32 0 0 8 0 0 0 0 0
1080 16 0 0 0 0 0 0 0 0
1081 16 1 1 0 0 0 4 3 3
1082 20 0 0 4 0 0 4 0 0
1083 4 0 0 0 0 0 4 1 1
1084 8 0 0 4 0 0 4 0 0
1085 8 0 0 0 0 0 4 0 0
1089 8 0 0 0 0 0 0 0 0
1090 12 0 0 6 0 0 2 0 0
1094 8 0 0 0 0 0 0 0 0
1095 28 1 1 4 0 0 4 0 0
1105 4 0 0 0 0 0 0 0 0
1108 3 0 0 1 1 1 0 0 0
1112 1 0 0 0 0 0 1 1 1
1113 3 0 0 2 0 0 1 0 0
1114 2 0 0 0 0 0 0 0 0
1115 1 0 0 0 0 0 0 0 0
1117 3 1 1 0 0 0 1 0 0
1118 2 0 0 1 0 0 1 0 0
1121 1 0 0 0 0 0 1 0 0
1125 4 0 0 1 0 0 0 0 0
1131 3 0 0 1 0 0 2 1 1
1132 1 0 0 0 0 0 0 0 0
1140 10 0 0 2 0 0 2 0 0
1147 4 1 1 2 0 0 2 0 0
1148 2 1 1 0 0 0 0 0 0
1151 4 0 0 2 0 0 2 1 1
1152 4 0 0 2 0 0 2 0 0
1153 2 0 0 0 0 0 0 0 0
1156 8 0 0 2 0 0 0 0 0
1165 4 0 0 0 0 0 0 0 0
1175 18 1 1 6 0 0 4 0 0
1187 8 1 1 4 0 0 0 0 0
1196 6 1 1 2 0 0 2 0 0
1203 4 1 1 0 0 0 0 0 0
1218 6 0 0 2 0 0 0 0 0
1237 4 0 0 2 0 0 2 0 0
1239 10 1 1 4 0 0 0 0 0
1293 6 0 0 2 1 1 0 0 0
1294 2 0 0 1 0 0 1 0 0
1297 8 0 0 2 0 0 2 0 0
1306 4 0 0 2 0 0 0 0 0
1308 8 1 1 4 0 0 2 0 0
1310 4 0 0 2 0 0 0 0 0
1326 4 0 0 0 0 0 2 0 0
1330 4 0 0 2 0 0 0 0 0
1331 4 0 0 2 0 0 0 0 0
1348 4 1 1 2 0 0 0 0 0
1349 1 0 0 0 0 0 1 0 0
1352 6 0 0 2 0 0 4 0 0
1357 4 0 0 2 0 0 0 0 0
1367 4 0 0 2 0 0 0 0 0
1377 6 1 1 2 0 0 2 0 0
1381 6 0 0 2 0 0 0 0 0
1401 18 0 0 14 0 0 0 0 0
fn=expand_dynamic_string_token
233 6 1 1 0 0 0 2 0 0
236 4 0 0 0 0 0 0 0 0
375 18 1 1 0 0 0 12 0 0
389 4 0 0 0 0 0 0 0 0
400 14 0 0 12 0 0 0 0 0
fn=fillin_rpath
444 16 2 2 0 0 0 12 0 0
446 1 0 0 0 0 0 0 0 0
448 12 0 0 4 0 0 2 0 0
455 2 1 1 1 0 0 0 0 0
457 4 0 0 1 0 0 1 0 0
461 2 0 0 0 0 0 0 0 0
466 2 0 0 0 0 0 1 0 0
467 2 0 0 0 0 0 0 0 0
474 7 2 2 1 0 0 0 0 0
479 4 0 0 0 0 0 2 0 0
483 17 1 1 5 0 0 0 0 0
484 8 0 0 4 0 0 0 0 0
502 4 3 3 1 0 0 1 0 0
505 1 1 1 0 0 0 1 0 0
506 7 0 0 2 0 0 2 0 0
508 3 0 0 1 0 0 0 0 0
512 2 0 0 0 0 0 2 1 1
513 1 0 0 0 0 0 0 0 0
514 4 0 0 0 0 0 2 0 0
515 2 0 0 1 0 0 1 0 0
517 2 0 0 1 0 0 0 0 0
523 4 1 1 1 0 0 0 0 0
524 40 2 2 1 0 0 1 0 0
525 12 1 1 0 0 0 5 0 0
527 2 0 0 1 0 0 1 0 0
528 3 1 1 1 0 0 0 0 0
533 2 1 1 0 0 0 1 0 0
535 1 0 0 0 0 0 1 0 0
536 1 0 0 0 0 0 1 0 0
539 3 0 0 0 0 0 1 0 0
541 3 0 0 1 0 0 1 0 0
545 1 0 0 0 0 0 1 0 0
548 9 0 0 7 0 0 0 0 0
fn=open_path
2003 8 1 1 0 0 0 6 0 0
2004 2 1 1 1 0 0 1 1 1
2007 1 0 0 0 0 0 1 0 0
2008 1 0 0 0 0 0 1 0 0
2010 2 0 0 0 0 0 0 0 0
2015 18 1 1 3 0 0 7 1 1
2018 3 1 1 2 0 0 0 0 0
2022 3 0 0 0 0 0 0 0 0
2027 4 0 0 0 0 0 1 0 0
2034 5 1 1 2 0 0 2 1 1
2035 35 0 0 0 0 0 0 0 0
2038 16 1 1 8 0 0 0 0 0
2042 80 0 0 48 0 0 16 0 0
2045 16 1 1 0 0 0 8 0 0
2048 24 0 0 8 0 0 0 0 0
2051 80 0 0 40 0 0 16 0 0
2053 40 1 1 24 0 0 0 0 0
2055 16 0 0 0 0 0 0 0 0
2060 16 1 1 8 0 0 0 0 0
2061 64 1 1 32 0 0 0 0 0
2067 62 1 1 26 0 0 9 0 0
2069 48 0 0 8 0 0 8 0 0
2070 2 0 0 1 1 1 0 0 0
2072 23 1 1 0 0 0 8 0 0
2089 2 0 0 0 0 0 1 0 0
2117 2 0 0 0 0 0 0 0 0
2120 7 2 2 1 0 0 0 0 0
2125 1 0 0 1 0 0 0 0 0
2127 4 0 0 3 0 0 0 0 0
2130 3 0 0 1 0 0 0 0 0
2144 9 2 2 7 0 0 0 0 0
fn=open_verify.constprop.7
1653 140 2 2 10 0 0 80 2 2
1692 48 0 0 10 0 0 0 0 0
1705 8 0 0 0 0 0 0 0 0
1723 40 0 0 0 0 0 10 1 1
1725 22 1 1 0 0 0 0 0 0
1730 8 0 0 0 0 0 0 0 0
1736 2 0 0 0 0 0 2 0 0
1737 6 0 0 0 0 0 4 0 0
1742 14 0 0 2 0 0 2 0 0
1744 4 0 0 0 0 0 0 0 0
1746 4 1 1 2 0 0 2 0 0
1748 4 0 0 0 0 0 0 0 0
1754 4 0 0 0 0 0 0 0 0
1770 34 3 3 19 2 2 0 0 0
1844 4 0 0 2 0 0 0 0 0
1849 4 1 1 2 0 0 0 0 0
1851 8 0 0 2 0 0 0 0 0
1857 4 0 0 0 0 0 0 0 0
1868 4 0 0 2 2 2 0 0 0
1874 8 0 0 2 0 0 0 0 0
1875 8 1 1 2 0 0 0 0 0
1876 4 0 0 2 0 0 0 0 0
1896 80 0 0 0 0 0 0 0 0
1898 38 1 1 17 10 10 0 0 0
1911 6 0 0 0 0 0 0 0 0
1914 8 1 1 4 0 0 0 0 0
1915 6 1 1 2 0 0 0 0 0
1939 18 1 1 12 2 2 0 0 0
1941 2 0 0 0 0 0 0 0 0
1942 24 2 2 4 0 0 0 0 0
1945 6 0 0 0 0 0 0 0 0
1950 1 0 0 0 0 0 0 0 0
1951 4 0 0 1 0 0 0 0 0
1954 2 0 0 0 0 0 0 0 0
1957 2 0 0 1 1 1 0 0 0
1958 4 1 1 1 0 0 0 0 0
1959 1 0 0 1 0 0 0 0 0
1960 3 0 0 1 0 0 0 0 0
1961 3 0 0 1 0 0 0 0 0
1985 6 1 1 0 0 0 2 0 0
1989 90 1 1 70 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-lookup.c
fn=_dl_lookup_symbol_x
554 180 0 0 0 0 0 0 0 0
555 5662 1 1 1393 81 78 0 0 0
556 5212 0 0 0 0 0 0 0 0
790 1260 2 2 90 0 0 810 6 2
792 180 0 0 0 0 0 90 3 1
793 180 0 0 0 0 0 90 0 0
796 90 0 0 90 2 0 0 0 0
800 432 0 0 171 0 0 0 0 0
804 990 1 1 180 0 0 360 0 0
805 270 1 1 90 3 0 0 0 0
811 318 0 0 106 0 0 0 0 0
813 1170 1 1 450 0 0 630 3 1
816 434 0 0 82 0 0 0 0 0
819 32 0 0 0 0 0 0 0 0
841 180 0 0 90 0 0 0 0 0
843 48 1 1 8 0 0 0 0 0
860 8 1 1 0 0 0 8 0 0
861 16 1 1 0 0 0 0 0 0
865 574 1 1 164 0 0 0 0 0
896 82 0 0 0 0 0 0 0 0
905 328 0 0 82 0 0 0 0 0
919 246 0 0 82 2 0 0 0 0
920 2 1 1 0 0 0 1 0 0
922 328 1 1 164 0 0 0 0 0
927 82 0 0 0 0 0 82 0 0
929 826 0 0 630 0 0 0 0 0
fn=_dl_setup_hash
939 12 1 1 4 0 0 0 0 0
943 4 0 0 4 0 0 0 0 0
947 8 0 0 4 4 4 4 1 1
948 4 0 0 4 0 0 0 0 0
949 4 0 0 4 1 1 0 0 0
951 12 0 0 0 0 0 0 0 0
952 4 0 0 0 0 0 4 0 0
953 12 0 0 4 0 0 4 0 0
955 4 1 1 0 0 0 4 0 0
956 8 0 0 0 0 0 0 0 0
958 4 0 0 0 0 0 4 0 0
960 12 0 0 0 0 0 4 0 0
961 4 0 0 4 0 0 0 0 0
fn=do_lookup_x
78 574 1 1 246 7 6 0 0 0
90 1019 0 0 0 0 0 430 0 0
93 308 0 0 154 0 0 36 0 0
97 82 0 0 82 0 0 0 0 0
98 164 1 1 82 0 0 0 0 0
100 162 0 0 0 0 0 0 0 0
119 81 0 0 81 7 3 0 0 0
120 729 1 1 324 3 0 0 0 0
121 810 2 2 324 0 0 243 1 1
148 2 1 1 0 0 0 0 0 0
150 5 0 0 2 0 0 0 0 0
180 35 1 1 20 0 0 0 0 0
294 203 0 0 0 0 0 0 0 0
338 1170 2 2 90 0 0 990 9 3
339 90 0 0 90 2 0 0 0 0
344 180 0 0 90 0 0 0 0 0
345 90 0 0 90 0 0 0 0 0
349 570 1 1 570 11 0 0 0 0
352 570 0 0 285 0 0 0 0 0
356 1110 0 0 90 0 0 90 0 0
360 570 1 1 285 7 0 0 0 0
364 570 0 0 285 2 0 0 0 0
370 855 0 0 285 6 0 0 0 0
374 87 0 0 0 0 0 87 0 0
375 87 1 1 0 0 0 87 0 0
378 570 0 0 570 14 0 0 0 0
379 855 1 1 570 3 0 285 0 0
382 285 0 0 285 0 0 0 0 0
383 570 0 0 0 0 0 0 0 0
385 285 0 0 285 45 33 0 0 0
386 180 1 1 0 0 0 90 0 0
387 570 0 0 570 0 0 0 0 0
390 1425 0 0 570 0 0 0 0 0
393 1995 1 1 0 0 0 0 0 0
396 174 0 0 174 46 43 0 0 0
397 261 1 1 0 0 0 0 0 0
398 174 0 0 0 0 0 0 0 0
400 261 0 0 87 0 0 87 0 0
403 890 1 1 356 58 56 0 0 0
405 328 0 0 82 0 0 0 0 0
406 246 0 0 82 14 12 0 0 0
407 164 0 0 0 0 0 0 0 0
413 288 0 0 0 0 0 0 0 0
421 180 0 0 0 0 0 0 0 0
446 10 1 1 5 0 0 0 0 0
452 820 1 1 410 0 0 0 0 0
503 164 0 0 0 0 0 0 0 0
506 620 1 1 82 0 0 0 0 0
510 27 0 0 9 1 0 0 0 0
522 492 2 2 246 0 0 246 0 0
524 82 0 0 0 0 0 0 0 0
540 1420 0 0 541 0 0 0 0 0
541 168 0 0 24 0 0 48 2 1
544 609 0 0 0 0 0 0 0 0
547 16 0 0 0 0 0 0 0 0
548 720 0 0 630 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-minimal.c
fn=calloc
92 8 1 1 0 0 0 0 0 0
96 8 0 0 0 0 0 0 0 0
99 16 0 0 0 0 0 0 0 0
100 24 0 0 0 0 0 0 0 0
103 8 0 0 0 0 0 0 0 0
fn=free
111 12 1 1 6 0 0 0 0 0
fn=malloc
49 3 0 0 0 0 0 2 0 0
50 87 1 1 43 0 0 0 0 0
55 3 0 0 0 0 0 1 0 0
56 2 2 2 1 0 0 0 0 0
57 2 0 0 0 0 0 0 0 0
61 66 0 0 0 0 0 22 0 0
64 150 1 1 0 0 0 0 0 0
69 4 0 0 1 0 0 0 0 0
70 2 0 0 0 0 0 0 0 0
72 1 0 0 0 0 0 0 0 0
73 8 1 1 0 0 0 1 0 0
75 2 0 0 0 0 0 0 0 0
77 3 0 0 1 0 0 0 0 0
79 3 0 0 0 0 0 1 0 0
82 22 0 0 0 0 0 22 0 0
83 22 0 0 0 0 0 22 0 0
85 47 0 0 24 0 0 0 0 0
fn=strsep
265 4 1 1 2 0 0 0 0 0
267 2 0 0 2 0 0 0 0 0
268 4 0 0 0 0 0 0 0 0
272 77 0 0 15 0 0 0 0 0
277 56 1 1 28 0 0 0 0 0
279 84 0 0 28 0 0 0 0 0
287 14 0 0 0 0 0 0 0 0
290 1 0 0 0 0 0 1 0 0
294 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-misc.c
fn=_dl_name_match_p
282 190 1 1 0 0 0 76 0 0
283 152 0 0 38 2 0 38 2 2
284 41 1 1 0 0 0 0 0 0
286 38 1 1 38 0 0 0 0 0
288 154 0 0 0 0 0 0 0 0
289 210 0 0 42 5 0 42 0 0
292 39 0 0 39 0 0 0 0 0
294 35 0 0 0 0 0 0 0 0
295 190 0 0 114 0 0 0 0 0
fn=_dl_sysdep_read_whole_file
44 8 1 1 0 0 0 4 0 0
47 3 0 0 0 0 0 1 0 0
48 2 0 0 0 0 0 0 0 0
50 7 1 1 0 0 0 1 0 0
52 2 0 0 1 0 0 1 0 0
55 2 0 0 0 0 0 0 0 0
57 8 1 1 0 0 0 1 0 0
68 2 0 0 0 0 0 1 0 0
71 7 0 0 5 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-object.c
fn=_dl_add_to_namespace_list
31 15 2 2 0 0 0 9 0 0
33 9 0 0 3 0 0 3 0 0
35 22 0 0 3 0 0 0 0 0
38 15 0 0 5 0 0 0 0 0
40 2 0 0 0 0 0 2 0 0
42 2 0 0 0 0 0 2 0 0
45 2 1 1 0 0 0 1 0 0
46 9 0 0 3 0 0 0 0 0
47 6 0 0 3 0 0 3 0 0
48 6 0 0 0 0 0 3 0 0
50 6 0 0 3 0 0 0 0 0
51 9 0 0 9 0 0 0 0 0
fn=_dl_new_object
59 39 1 1 0 0 0 24 2 2
60 18 0 0 0 0 0 9 2 2
66 18 1 1 3 0 0 0 0 0
68 6 0 0 0 0 0 0 0 0
73 15 0 0 0 0 0 6 0 0
76 6 0 0 0 0 0 0 0 0
79 3 0 0 0 0 0 3 2 2
80 9 1 1 3 0 0 3 3 3
84 6 0 0 0 0 0 3 1 1
85 24 1 1 9 0 0 9 2 2
87 3 0 0 0 0 0 3 0 0
95 18 0 0 6 0 0 3 1 1
96 15 0 0 3 3 3 3 0 0
99 6 1 1 3 0 0 0 0 0
100 8 2 2 2 0 0 3 3 3
101 3 0 0 0 0 0 3 1 1
105 3 0 0 0 0 0 3 0 0
108 43 0 0 0 0 0 0 0 0
110 32 0 0 0 0 0 16 4 4
120 6 0 0 0 0 0 3 1 1
121 3 0 0 0 0 0 3 3 3
124 1 1 1 0 0 0 0 0 0
126 18 1 1 3 0 0 0 0 0
128 6 0 0 0 0 0 2 1 1
131 8 0 0 0 0 0 0 0 0
135 6 0 0 2 0 0 0 0 0
139 11 1 1 0 0 0 0 0 0
147 1 0 0 0 0 0 1 0 0
150 6 1 1 0 0 0 3 0 0
153 9 0 0 0 0 0 3 0 0
155 8 0 0 2 0 0 4 0 0
159 8 0 0 2 0 0 0 0 0
163 8 1 1 0 0 0 2 0 0
164 4 0 0 0 0 0 0 0 0
172 2 0 0 0 0 0 0 0 0
176 2 0 0 0 0 0 0 0 0
209 48 1 1 2 0 0 2 0 0
214 42 0 0 0 0 0 0 0 0
215 88 0 0 42 0 0 0 0 0
220 4 0 0 0 0 0 2 0 0
223 2 0 0 0 0 0 2 0 0
227 27 0 0 21 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-open.c
fn=_dl_find_dso_for_object
176 5 1 1 0 0 0 4 0 0
180 6 1 1 1 0 0 0 0 0
181 10 1 1 3 0 0 0 0 0
182 12 0 0 6 0 0 0 0 0
183 2 0 0 1 0 0 0 0 0
186 2 0 0 1 0 0 0 0 0
190 7 1 1 5 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-reloc.c
fn=_dl_relocate_object
148 48 1 1 0 0 0 32 0 0
155 4 0 0 0 0 0 4 0 0
158 6 0 0 0 0 0 0 0 0
159 12 0 0 0 0 0 8 0 0
163 8 0 0 0 0 0 0 0 0
164 20 1 1 4 1 0 4 0 0
170 12 0 0 8 0 0 0 0 0
176 16 0 0 4 0 0 0 0 0
177 8 0 0 4 3 0 0 0 0
180 9 2 2 0 0 0 0 0 0
187 8 0 0 4 0 0 0 0 0
231 12 0 0 8 0 0 4 0 0
258 190 3 3 80 13 0 42 0 0
261 16 0 0 4 0 0 0 0 0
285 4 0 0 4 0 0 0 0 0
288 8 0 0 4 0 0 0 0 0
305 12 1 1 4 3 0 0 0 0
307 32 0 0 28 1 0 0 0 0
313 24 0 0 12 0 0 0 0 0
316 8 0 0 0 0 0 0 0 0
320 8 0 0 0 0 0 0 0 0
321 20 1 1 0 0 0 4 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-sort-maps.c
fn=_dl_sort_maps
28 18 1 1 0 0 0 14 0 0
30 4 0 0 0 0 0 0 0 0
33 2 0 0 0 0 0 0 0 0
34 20 2 1 0 0 0 6 0 0
35 42 2 1 2 0 0 12 0 0
39 24 0 0 6 0 0 12 0 0
40 18 0 0 12 0 0 0 0 0
42 12 0 0 6 0 0 0 0 0
46 12 1 0 6 0 0 0 0 0
54 48 2 1 22 0 0 0 0 0
56 18 0 0 12 0 0 0 0 0
57 14 0 0 0 0 0 0 0 0
59 18 2 1 6 1 0 0 0 0
60 12 0 0 0 0 0 0 0 0
90 33 4 3 9 0 0 0 0 0
115 30 1 1 10 0 0 0 0 0
118 40 2 1 8 0 0 4 0 0
122 26 2 1 14 0 0 4 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-tunables.c
fn=__GI___tunables_init
68 305 0 0 61 0 0 0 0 0
71 60 0 0 0 0 0 0 0 0
74 5120 1 1 740 27 27 0 0 0
78 120 0 0 0 0 0 0 0 0
83 120 0 0 0 0 0 0 0 0
150 4 1 1 0 0 0 2 1 1
280 3 0 0 1 0 0 0 0 0
289 8 1 1 0 0 0 6 1 1
297 120 1 1 0 0 0 0 0 0
312 5340 2 2 0 0 0 0 0 0
318 6600 0 0 2640 0 0 0 0 0
330 240 1 1 60 0 0 0 0 0
364 8 0 0 7 0 0 0 0 0
fn=__tunable_get_val
373 168 2 1 17 10 0 0 0 0
377 31 1 1 17 3 0 14 0 0
382 3 0 0 0 0 0 3 0 0
383 3 0 0 0 0 0 0 0 0
399 85 1 0 17 1 0 0 0 0
401 17 0 0 17 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-tunables.h
fn=__GI___tunables_init
120 2523 0 0 1195 8 8 0 0 0
121 2536 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/dl-version.c
fn=_dl_check_all_versions
362 8 2 2 0 0 0 4 0 0
364 1 0 0 0 0 0 0 0 0
366 15 1 1 4 0 0 0 0 0
368 40 0 0 4 0 0 4 0 0
371 7 0 0 5 0 0 0 0 0
fn=_dl_check_map_versions
37 24 1 1 4 0 0 0 0 0
38 5 0 0 5 0 0 0 0 0
39 35 1 1 0 0 0 7 0 0
57 9 0 0 6 0 0 3 0 0
65 9 0 0 3 0 0 0 0 0
71 9 0 0 3 0 0 0 0 0
87 3 0 0 3 0 0 0 0 0
88 6 1 1 0 0 0 0 0 0
90 3 0 0 3 0 0 0 0 0
95 32 0 0 10 2 2 3 0 0
109 20 0 0 10 0 0 0 0 0
111 3 1 1 3 0 0 0 0 0
114 28 0 0 11 0 0 5 0 0
121 21 0 0 7 3 3 0 0 0
125 7 0 0 0 0 0 0 0 0
143 12 0 0 2 0 0 6 0 0
156 28 2 2 0 0 0 24 0 0
157 6 0 0 0 0 0 4 0 0
165 4 1 1 0 0 0 4 0 0
171 12 0 0 4 0 0 0 0 0
173 20 0 0 4 0 0 12 0 0
175 8 0 0 4 0 0 4 0 0
176 8 0 0 4 0 0 4 0 0
178 8 1 1 0 0 0 0 0 0
181 8 0 0 4 0 0 2 0 0
185 6 0 0 2 2 2 0 0 0
201 4 0 0 4 0 0 0 0 0
209 6 0 0 2 0 0 0 0 0
214 6 0 0 4 2 2 0 0 0
218 32 1 1 23 0 0 3 0 0
220 3 0 0 3 0 0 0 0 0
222 7 1 1 3 0 0 3 0 0
225 12 1 1 3 0 0 0 0 0
228 9 0 0 3 0 0 0 0 0
233 1 0 0 0 0 0 0 0 0
237 8 1 1 4 0 0 0 0 0
251 11 2 2 4 0 0 0 0 0
254 8 0 0 8 0 0 0 0 0
257 140 0 0 34 9 9 2 0 0
260 106 0 0 34 5 5 2 0 0
264 32 0 0 0 0 0 0 0 0
268 9 2 2 3 0 0 0 0 0
273 3 0 0 0 0 0 3 0 0
274 12 1 1 0 0 0 3 0 0
275 6 0 0 0 0 0 0 0 0
285 3 0 0 0 0 0 3 0 0
288 9 0 0 6 1 0 3 0 0
290 9 1 1 3 0 0 0 0 0
293 8 0 0 6 0 0 0 0 0
297 6 0 0 2 0 0 0 0 0
300 9 0 0 3 0 0 0 0 0
302 9 1 1 0 0 0 0 0 0
304 15 0 0 3 0 0 3 0 0
305 9 0 0 0 0 0 3 2 2
306 9 0 0 3 0 0 3 0 0
307 9 0 0 3 0 0 3 0 0
310 9 1 1 3 0 0 0 0 0
315 1 0 0 0 0 0 0 0 0
318 6 0 0 2 0 0 0 0 0
328 9 0 0 3 0 0 0 0 0
331 8 0 0 6 0 0 0 0 0
335 32 0 0 32 0 0 0 0 0
337 68 0 0 34 0 0 0 0 0
341 32 0 0 32 0 0 0 0 0
342 160 0 0 32 0 0 32 10 10
343 96 0 0 32 0 0 32 0 0
344 32 0 0 0 0 0 32 3 3
347 102 0 0 34 0 0 0 0 0
351 32 0 0 0 0 0 0 0 0
357 36 0 0 32 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/do-rel.h
fn=_dl_relocate_object
47 24 1 1 8 0 0 8 0 0
48 8 0 0 8 0 0 0 0 0
50 11 0 0 0 0 0 3 0 0
51 6 0 0 0 0 0 4 0 0
58 24 0 0 8 0 0 0 0 0
61 145 1 1 0 0 0 0 0 0
63 188 1 1 47 17 17 0 0 0
65 119 1 1 0 0 0 0 0 0
74 4 0 0 0 0 0 0 0 0
75 142 2 2 17 0 0 0 0 0
76 78 0 0 39 0 0 0 0 0
83 12 0 0 6 0 0 6 0 0
84 6 0 0 6 0 0 0 0 0
86 24 1 1 12 0 0 0 0 0
98 18 0 0 0 0 0 0 0 0
108 8 0 0 0 0 0 0 0 0
111 3741 1 1 0 0 0 0 0 0
112 2488 0 0 1244 0 0 0 0 0
118 18 0 0 6 4 0 0 0 0
121 10 1 1 5 2 0 5 0 0
124 319 0 0 108 1 0 0 0 0
127 412 1 1 103 27 24 0 0 0
136 412 0 0 206 41 38 0 0 0
137 412 1 1 103 0 0 103 0 0
138 352 0 0 103 1 0 0 0 0
139 309 0 0 206 0 0 103 0 0
143 15 1 1 6 0 0 0 0 0
160 22 1 1 8 0 0 2 0 0
162 20 0 0 5 1 1 0 0 0
170 30 0 0 5 0 0 5 0 0
171 15 1 1 10 0 0 5 0 0
174 2 1 1 0 0 0 0 0 0
fn=_dl_start
83 1 0 0 1 0 0 0 0 0
84 1 0 0 1 0 0 0 0 0
111 120 0 0 0 0 0 0 0 0
112 78 0 0 39 5 5 0 0 0
116 2 0 0 1 0 0 0 0 0
124 31 0 0 0 0 0 0 0 0
136 27 1 1 9 2 2 0 0 0
137 18 0 0 0 0 0 0 0 0
139 18 0 0 9 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/get-dynamic-info.h
fn=_dl_map_object_from_fd
42 4 0 0 0 0 0 0 0 0
46 2 0 0 0 0 0 0 0 0
48 141 0 0 47 13 13 0 0 0
50 90 0 0 0 0 0 0 0 0
63 42 0 0 0 0 0 0 0 0
64 71 1 1 0 0 0 43 11 11
65 8 1 1 0 0 0 0 0 0
67 2 0 0 0 0 0 0 0 0
68 10 2 2 0 0 0 0 0 0
70 2 0 0 0 0 0 0 0 0
71 10 0 0 0 0 0 0 0 0
72 2 0 0 0 0 0 0 0 0
73 8 0 0 0 0 0 2 0 0
74 45 0 0 0 0 0 0 0 0
81 4 1 1 0 0 0 0 0 0
101 7 0 0 3 0 0 0 0 0
102 8 0 0 4 0 0 0 0 0
103 8 1 1 4 0 0 0 0 0
104 8 0 0 4 0 0 0 0 0
106 8 0 0 4 0 0 0 0 0
111 8 0 0 4 0 0 0 0 0
112 7 1 1 3 1 1 0 0 0
113 8 0 0 4 0 0 0 0 0
119 6 0 0 2 0 0 0 0 0
124 4 0 0 2 0 0 0 0 0
131 4 0 0 2 0 0 0 0 0
132 6 1 1 4 0 0 0 0 0
150 6 0 0 2 1 1 0 0 0
155 2 0 0 1 0 0 1 0 0
157 2 0 0 0 0 0 0 0 0
159 2 0 0 0 0 0 0 0 0
161 2 0 0 0 0 0 0 0 0
164 6 1 1 2 0 0 0 0 0
166 4 0 0 1 0 0 1 0 0
174 2 0 0 1 0 0 0 0 0
179 2 0 0 0 0 0 0 0 0
182 4 0 0 2 0 0 0 0 0
fn=_dl_start
48 57 1 1 19 6 6 0 0 0
50 36 1 1 0 0 0 0 0 0
63 21 0 0 0 0 0 0 0 0
64 29 0 0 0 0 0 17 5 5
65 4 0 0 0 0 0 0 0 0
67 3 0 0 0 0 0 0 0 0
68 5 1 1 0 0 0 0 0 0
70 2 0 0 0 0 0 0 0 0
71 5 1 1 0 0 0 0 0 0
72 1 0 0 0 0 0 0 0 0
73 5 1 1 0 0 0 1 1 1
74 18 0 0 0 0 0 0 0 0
81 2 1 1 0 0 0 0 0 0
101 4 0 0 2 0 0 0 0 0
102 4 0 0 2 0 0 0 0 0
103 4 1 1 2 0 0 0 0 0
104 4 0 0 2 0 0 0 0 0
106 4 0 0 2 0 0 0 0 0
111 4 0 0 2 0 0 0 0 0
112 4 1 1 2 0 0 0 0 0
113 4 0 0 2 0 0 0 0 0
119 3 0 0 1 0 0 0 0 0
124 2 0 0 1 0 0 0 0 0
131 3 0 0 1 0 0 0 0 0
132 3 1 1 2 0 0 0 0 0
140 3 0 0 1 0 0 0 0 0
143 3 0 0 1 1 1 0 0 0
147 2 1 1 1 0 0 0 0 0
148 2 0 0 1 0 0 0 0 0
fn=dl_main
33 1 0 0 1 0 0 0 0 0
42 2 0 0 0 0 0 0 0 0
46 1 0 0 0 0 0 0 0 0
48 81 0 0 27 7 7 0 0 0
50 52 0 0 0 0 0 0 0 0
63 25 1 1 0 0 0 0 0 0
64 41 1 1 0 0 0 25 6 6
65 4 0 0 0 0 0 0 0 0
67 1 0 0 0 0 0 0 0 0
68 5 0 0 0 0 0 0 0 0
70 1 0 0 0 0 0 0 0 0
71 5 0 0 0 0 0 0 0 0
72 1 1 1 0 0 0 0 0 0
73 4 0 0 0 0 0 1 0 0
74 26 0 0 0 0 0 0 0 0
81 3 0 0 1 0 0 0 0 0
101 3 0 0 1 0 0 0 0 0
102 4 0 0 2 0 0 0 0 0
103 4 1 1 2 0 0 0 0 0
104 4 0 0 2 0 0 0 0 0
106 4 0 0 2 0 0 0 0 0
111 4 0 0 2 0 0 0 0 0
112 4 1 1 2 0 0 0 0 0
113 4 0 0 2 0 0 0 0 0
119 3 0 0 1 0 0 0 0 0
124 2 0 0 1 0 0 0 0 0
131 2 0 0 1 0 0 0 0 0
132 3 1 1 2 0 0 0 0 0
150 3 0 0 1 0 0 0 0 0
155 2 0 0 1 0 0 1 1 1
157 2 0 0 0 0 0 0 0 0
159 2 0 0 0 0 0 0 0 0
161 2 0 0 0 0 0 0 0 0
162 1 0 0 0 0 0 1 0 0
164 3 1 1 1 0 0 0 0 0
166 3 0 0 1 0 0 1 0 0
174 2 0 0 1 0 0 0 0 0
179 2 0 0 0 0 0 0 0 0
180 2 0 0 1 0 0 1 0 0
182 2 1 1 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/rtld.c
fn=_dl_start
393 2 0 0 0 0 0 1 1 1
394 2 0 0 0 0 0 1 0 0
395 2 0 0 0 0 0 1 0 0
396 2 0 0 0 0 0 1 0 0
397 2 0 0 0 0 0 1 1 1
405 5 1 1 0 0 0 1 0 0
408 1 0 0 0 0 0 1 0 0
414 4 1 0 0 0 0 1 0 0
423 4 0 0 0 0 0 0 0 0
426 2 0 0 1 1 0 1 1 0
430 2 1 0 1 0 0 0 0 0
444 9 1 1 0 0 0 6 1 1
463 5 0 0 0 0 0 1 1 1
486 1 0 0 0 0 0 1 1 1
489 1 0 0 0 0 0 1 1 1
500 2 0 0 0 0 0 0 0 0
505 27 3 3 9 0 0 0 0 0
507 1 1 1 1 1 1 0 0 0
532 9 0 0 7 1 0 0 0 0
fn=dl_main
799 1 0 0 1 0 0 0 0 0
801 1 1 1 0 0 0 1 0 0
810 1 0 0 0 0 0 1 0 0
812 1 0 0 0 0 0 1 0 0
817 1 0 0 0 0 0 1 0 0
870 12 2 2 0 0 0 7 1 1
876 1 1 1 0 0 0 0 0 0
879 1 0 0 0 0 0 0 0 0
885 1 0 0 0 0 0 1 0 0
887 2 0 0 0 0 0 1 1 1
891 2 0 0 0 0 0 1 1 1
892 2 0 0 0 0 0 1 0 0
897 2 1 1 0 0 0 1 0 0
907 3 1 1 1 0 0 0 0 0
1108 8 1 1 0 0 0 1 0 0
1110 2 0 0 0 0 0 0 0 0
1111 1 0 0 0 0 0 1 0 0
1112 2 1 1 1 0 0 1 0 0
1113 2 0 0 1 0 0 1 0 0
1117 3 0 0 0 0 0 1 0 0
1118 2 0 0 1 0 0 0 0 0
1139 1 1 1 0 0 0 1 0 0
1140 1 0 0 0 0 0 1 0 0
1142 1 0 0 0 0 0 1 0 0
1144 1 0 0 1 0 0 0 0 0
1147 33 0 0 1 0 0 0 0 0
1148 71 1 1 9 5 5 0 0 0
1152 3 1 1 1 0 0 1 0 0
1153 1 0 0 0 0 0 0 0 0
1157 3 0 0 2 0 0 1 0 0
1158 1 0 0 0 0 0 0 0 0
1166 2 0 0 0 0 0 1 1 1
1167 2 2 2 2 1 1 0 0 0
1169 1 0 0 0 0 0 1 0 0
1176 2 0 0 1 0 0 0 0 0
1188 1 0 0 0 0 0 0 0 0
1194 2 0 0 0 0 0 0 0 0
1202 4 0 0 2 0 0 0 0 0
1203 10 1 1 3 1 1 0 0 0
1204 4 1 1 2 0 0 0 0 0
1205 1 0 0 0 0 0 1 0 0
1208 4 0 0 2 1 1 0 0 0
1209 4 0 0 2 0 0 0 0 0
1210 2 0 0 0 0 0 2 0 0
1211 6 0 0 3 0 0 0 0 0
1212 2 1 1 0 0 0 1 0 0
1239 2 0 0 1 0 0 1 0 0
1240 1 0 0 0 0 0 0 0 0
1243 2 0 0 1 0 0 1 0 0
1244 2 0 0 1 0 0 1 0 0
1245 1 0 0 0 0 0 0 0 0
1250 3 1 1 1 1 1 0 0 0
1253 2 0 0 1 0 0 0 0 0
1255 2 1 1 1 0 0 0 0 0
1257 3 0 0 1 0 0 0 0 0
1270 3 0 0 1 0 0 0 0 0
1271 6 0 0 1 0 0 2 0 0
1273 3 1 1 3 0 0 0 0 0
1276 2 0 0 1 0 0 1 0 0
1278 1 0 0 0 0 0 1 0 0
1279 1 0 0 0 0 0 1 0 0
1281 2 1 1 1 0 0 0 0 0
1282 2 0 0 0 0 0 1 0 0
1286 2 0 0 1 0 0 0 0 0
1288 2 0 0 0 0 0 0 0 0
1293 2 0 0 0 0 0 1 0 0
1296 2 0 0 1 0 0 0 0 0
1312 5 1 1 0 0 0 2 0 0
1318 10 2 2 1 0 0 2 0 0
1323 2 1 1 1 0 0 1 0 0
1326 4 0 0 1 0 0 2 0 0
1328 1 0 0 0 0 0 1 0 0
1333 2 0 0 1 0 0 0 0 0
1336 3 0 0 2 0 0 1 0 0
1337 4 1 1 1 0 0 1 0 0
1338 2 0 0 1 0 0 1 0 0
1339 1 0 0 0 0 0 1 0 0
1340 1 0 0 1 0 0 0 0 0
1341 1 0 0 1 0 0 0 0 0
1346 2 0 0 1 0 0 0 0 0
1347 5 1 1 1 0 0 1 0 0
1364 2 0 0 1 1 1 0 0 0
1365 2 0 0 1 0 0 0 0 0
1367 3 1 1 1 0 0 0 0 0
1369 1 0 0 0 0 0 1 0 0
1370 3 0 0 1 0 0 1 0 0
1375 4 0 0 0 0 0 0 0 0
1376 5 0 0 1 1 1 0 0 0
1378 2 1 1 1 0 0 1 1 1
1379 2 0 0 1 0 0 1 0 0
1384 2 1 1 1 1 1 0 0 0
1389 1 0 0 0 0 0 1 0 0
1390 4 0 0 2 0 0 0 0 0
1391 2 1 1 0 0 0 0 0 0
1570 2 0 0 0 0 0 2 0 0
1578 3 0 0 1 0 0 0 0 0
1581 2 0 0 1 0 0 1 0 0
1585 3 0 0 1 0 0 0 0 0
1590 2 1 1 1 0 0 1 0 0
1591 1 0 0 0 0 0 1 0 0
1592 1 0 0 0 0 0 0 0 0
1596 2 0 0 1 0 0 0 0 0
1611 3 0 0 2 0 0 0 0 0
1612 1 0 0 0 0 0 0 0 0
1613 1 0 0 0 0 0 0 0 0
1615 3 0 0 1 0 0 0 0 0
1617 5 1 1 0 0 0 0 0 0
1618 3 0 0 0 0 0 1 0 0
1619 4 0 0 0 0 0 0 0 0
1621 2 0 0 1 0 0 0 0 0
1631 5 1 1 0 0 0 1 0 0
1708 4 0 0 2 0 0 0 0 0
1712 8 2 2 0 0 0 0 0 0
1713 1 0 0 0 0 0 0 0 0
1716 3 0 0 0 0 0 1 0 0
1717 1 0 0 1 0 0 0 0 0
1718 2 0 0 0 0 0 0 0 0
1719 2 0 0 0 0 0 0 0 0
1725 5 0 0 0 0 0 0 0 0
1726 8 1 1 1 0 0 1 0 0
1727 4 0 0 0 0 0 0 0 0
1729 2 0 0 1 0 0 0 0 0
1732 11 0 0 1 0 0 0 0 0
1733 16 1 1 9 0 0 0 0 0
1736 3 0 0 2 0 0 1 0 0
1737 3 0 0 1 0 0 0 0 0
1738 1 0 0 0 0 0 1 0 0
1740 12 0 0 0 0 0 0 0 0
1741 11 1 1 7 0 0 0 0 0
1751 2 1 1 0 0 0 1 0 0
1753 3 1 1 1 0 0 1 0 0
1754 2 0 0 1 0 0 0 0 0
1756 2 1 1 0 0 0 1 0 0
1758 3 0 0 0 0 0 0 0 0
1760 3 0 0 1 0 0 0 0 0
1774 4 0 0 3 0 0 0 0 0
1775 2 0 0 1 0 0 1 0 0
1776 3 0 0 1 0 0 0 0 0
1787 4 1 1 1 0 0 1 0 0
1788 1 0 0 0 0 0 1 1 1
1789 6 1 1 0 0 0 2 0 0
1799 2 0 0 1 0 0 1 0 0
1800 2 0 0 1 0 0 0 0 0
1801 2 0 0 0 0 0 2 0 0
1803 2 0 0 1 0 0 0 0 0
1808 2 0 0 1 0 0 0 0 0
2038 3 0 0 1 1 1 0 0 0
2094 2 1 1 0 0 0 1 0 0
2098 2 0 0 1 0 0 1 0 0
2104 2 1 1 1 0 0 1 0 0
2107 2 0 0 1 0 0 0 0 0
2161 3 1 1 1 0 0 0 0 0
2168 1 0 0 1 0 0 0 0 0
2170 5 0 0 0 0 0 0 0 0
2171 1 1 1 1 0 0 0 0 0
2172 18 0 0 0 0 0 0 0 0
2174 8 0 0 8 1 0 0 0 0
2179 8 0 0 8 0 0 0 0 0
2181 10 0 0 0 0 0 0 0 0
2183 1 1 1 0 0 0 1 0 0
2184 1 0 0 1 0 0 0 0 0
2187 4 0 0 4 0 0 0 0 0
2189 8 1 1 4 1 0 0 0 0
2190 24 0 0 6 2 0 3 0 0
2194 10 0 0 5 1 0 0 0 0
2195 3 1 1 0 0 0 1 0 0
2197 4 2 2 0 0 0 0 0 0
2199 3 0 0 0 0 0 1 1 0
2205 2 0 0 1 0 0 0 0 0
2210 4 1 1 2 0 0 0 0 0
2212 1 0 0 1 0 0 0 0 0
2219 3 0 0 1 0 0 1 0 0
2222 2 0 0 1 0 0 0 0 0
2231 3 0 0 2 0 0 0 0 0
2233 4 1 1 1 0 0 0 0 0
2248 5 0 0 0 0 0 0 0 0
2250 1 0 0 1 0 0 0 0 0
2251 5 0 0 1 0 0 1 0 0
2252 4 1 1 0 0 0 0 0 0
2254 2 0 0 1 0 0 0 0 0
2262 1 0 0 0 0 0 1 0 0
2266 2 0 0 1 0 0 0 0 0
2286 4 0 0 0 0 0 1 0 0
2287 1 0 0 0 0 0 1 0 0
2288 1 0 0 0 0 0 1 0 0
2289 1 0 0 0 0 0 0 0 0
2293 1 0 0 0 0 0 1 0 0
2298 8 1 1 7 2 0 0 0 0
2464 2 0 0 1 0 0 1 1 1
2466 1 0 0 0 0 0 1 0 0
2467 1 0 0 0 0 0 0 0 0
2471 8 1 1 1 0 0 2 0 0
2473 25 0 0 5 0 0 5 1 1
2475 4 0 0 0 0 0 0 0 0
2477 165 1 1 33 0 0 0 0 0
2478 29 0 0 0 0 0 0 0 0
2480 8 0 0 0 0 0 0 0 0
2486 24 0 0 3 1 1 0 0 0
2507 4 1 1 2 0 0 0 0 0
2514 12 0 0 0 0 0 2 0 0
2516 3 0 0 0 0 0 1 0 0
2521 6 2 2 0 0 0 1 0 0
2562 3 1 1 1 0 0 0 0 0
2563 6 1 1 0 0 0 1 0 0
2565 3 1 1 0 0 0 1 1 1
2635 3 1 1 1 0 0 0 0 0
2667 3 0 0 1 0 0 0 0 0
fn=handle_ld_preload
121 3 0 0 1 0 0 0 0 0
752 1 0 0 0 0 0 1 0 0
756 1 0 0 0 0 0 1 0 0
757 1 0 0 0 0 0 1 0 0
758 1 0 0 0 0 0 1 0 0
760 1 0 0 1 0 0 0 0 0
762 11 1 1 2 0 0 3 1 1
763 3 0 0 1 0 0 0 0 0
771 4 0 0 1 0 0 0 0 0
837 9 1 1 0 0 0 6 0 0
838 1 0 0 0 0 0 0 0 0
842 4 0 0 2 0 0 0 0 0
845 4 0 0 0 0 0 1 0 0
846 3 1 1 0 0 0 0 0 0
848 5 2 2 0 0 0 1 0 0
849 2 1 1 0 0 0 1 0 0
855 1 0 0 0 0 0 0 0 0
857 2 0 0 1 0 0 0 0 0
859 2 0 0 1 0 0 0 0 0
863 9 0 0 7 0 0 0 0 0
fn=init_tls
681 1 0 0 0 0 0 1 0 0
683 2 0 0 1 0 0 1 0 0
687 2 0 0 1 0 0 0 0 0
693 2 0 0 0 0 0 1 0 0
696 1 0 0 0 0 0 1 0 0
697 4 0 0 0 0 0 1 0 0
702 1 0 0 0 0 0 0 0 0
704 1 0 0 0 0 0 1 1 1
708 2 1 1 1 1 1 0 0 0
709 1 0 0 0 0 0 0 0 0
710 16 1 1 1 0 0 0 0 0
711 8 0 0 4 0 0 0 0 0
712 8 0 0 4 0 0 0 0 0
716 2 0 0 0 0 0 1 0 0
718 1 0 0 0 0 0 0 0 0
720 2 0 0 0 0 0 0 0 0
723 1 1 1 0 0 0 1 0 0
730 2 0 0 0 0 0 1 0 0
731 2 0 0 0 0 0 0 0 0
737 2 1 1 1 0 0 1 0 0
740 7 0 0 0 0 0 2 0 0
743 1 1 1 0 0 0 1 0 0
745 1 0 0 0 0 0 0 0 0
746 3 0 0 2 0 0 0 0 0
fn=map_doit
588 2 1 1 0 0 0 1 0 0
590 4 0 0 1 0 0 0 0 0
591 6 1 1 2 0 0 2 0 0
593 2 0 0 2 0 0 0 0 0
fn=rtld_lock_default_lock_recursive
784 5 1 1 5 2 1 0 0 0
785 5 0 0 5 0 0 0 0 0
fn=rtld_lock_default_unlock_recursive
790 5 0 0 5 1 0 0 0 0
791 5 0 0 5 0 0 0 0 0
fn=version_check_doit
621 2 1 1 0 0 0 1 0 0
623 6 0 0 2 0 0 1 0 0
627 2 1 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/elf/setup-vdso.h
fn=dl_main
24 2 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/access.c
fn=access
27 7 1 1 0 0 0 1 0 0
31 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/close.c
fn=close
27 12 1 1 0 0 0 0 0 0
28 3 0 0 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/open64.c
fn=open
36 11 0 0 0 0 0 11 1 1
39 66 0 0 0 0 0 0 0 0
47 101 2 2 0 0 0 8 0 0
49 11 0 0 11 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/read.c
fn=read
27 8 1 1 0 0 0 0 0 0
28 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/fxstat.c
fn=_fxstat
33 4 0 0 0 0 0 0 0 0
34 8 2 2 0 0 0 0 0 0
35 24 0 0 0 0 0 0 0 0
39 4 0 0 4 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/lxstat.c
fn=open
39 11 1 1 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/wordsize-64/xstat.c
fn=_xstat
33 8 0 0 0 0 0 0 0 0
34 16 1 1 0 0 0 0 0 0
35 76 0 0 7 0 0 7 0 0
39 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/io/../sysdeps/unix/sysv/linux/write.c
fn=write
27 24 1 1 3 0 0 0 0 0
28 3 0 0 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/../misc/sys/sysmacros.h
fn=_IO_file_doallocate
79 6 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/filedoalloc.c
fn=_IO_file_doallocate
78 8 2 2 1 0 0 4 1 0
84 9 1 1 3 0 0 1 1 0
86 4 0 0 1 0 0 0 0 0
89 2 0 0 0 0 0 0 0 0
91 2 1 1 1 1 0 0 0 0
94 2 0 0 1 0 0 0 0 0
97 4 0 0 1 0 0 0 0 0
101 3 0 0 0 0 0 1 0 0
102 2 0 0 0 0 0 0 0 0
103 1 0 0 0 0 0 0 0 0
104 4 1 1 0 0 0 1 0 0
105 1 0 0 0 0 0 0 0 0
106 8 0 0 6 2 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/fileops.c
fn=_IO_do_write@@GLIBC_2.2.5
431 48 1 1 3 0 0 18 0 0
433 24 1 1 0 0 0 0 0 0
434 25 0 0 22 0 0 0 0 0
442 6 1 1 3 0 0 0 0 0
449 12 0 0 6 0 0 0 0 0
457 15 0 0 3 1 0 3 0 0
458 15 0 0 3 0 0 0 0 0
460 12 0 0 3 0 0 9 0 0
461 6 0 0 0 0 0 6 0 0
462 3 0 0 0 0 0 3 0 0
463 6 1 1 3 0 0 0 0 0
464 9 1 1 3 0 0 0 0 0
fn=_IO_file_overflow@@GLIBC_2.2.5
746 1284 0 0 214 0 0 642 0 0
747 642 1 1 214 0 0 0 0 0
754 1067 0 0 213 0 0 0 0 0
757 2 1 1 0 0 0 0 0 0
759 2 1 1 0 0 0 1 1 0
760 6 0 0 2 0 0 3 0 0
769 2 0 0 0 0 0 0 0 0
778 4 0 0 2 0 0 0 0 0
780 1 1 1 0 0 0 1 0 0
781 2 0 0 0 0 0 1 0 0
782 1 0 0 0 0 0 1 0 0
783 2 0 0 0 0 0 2 0 0
785 3 0 0 0 0 0 1 0 0
786 5 0 0 1 1 0 0 0 0
787 1 0 0 0 0 0 1 0 0
789 428 1 1 0 0 0 0 0 0
790 8 0 0 0 0 0 0 0 0
791 4 0 0 0 0 0 0 0 0
792 420 0 0 210 0 0 0 0 0
795 630 0 0 0 0 0 420 0 0
796 630 0 0 210 0 0 0 0 0
797 1050 0 0 0 0 0 0 0 0
802 852 0 0 852 1 0 0 0 0
fn=_IO_file_setbuf@@GLIBC_2.2.5
389 2 1 1 0 0 0 1 0 0
390 3 0 0 0 0 0 1 0 0
393 2 0 0 0 0 0 2 0 0
394 2 0 0 1 0 0 1 0 0
395 3 1 1 0 0 0 3 0 0
397 1 0 0 0 0 0 0 0 0
398 2 0 0 2 0 0 0 0 0
fn=_IO_file_stat
1169 1 1 1 0 0 0 0 0 0
1170 3 0 0 1 0 0 0 0 0
fn=_IO_file_sync@@GLIBC_2.2.5
807 4 1 1 0 0 0 2 0 0
812 4 0 0 2 0 0 0 0 0
814 1 1 1 1 0 0 0 0 0
815 2 0 0 1 0 0 0 0 0
830 2 2 2 0 0 0 1 0 0
834 4 0 0 3 0 0 0 0 0
fn=_IO_file_write@@GLIBC_2.2.5
1196 18 0 0 0 0 0 12 0 0
1198 24 1 1 0 0 0 0 0 0
1203 18 0 0 6 0 0 3 1 0
1204 6 0 0 0 0 0 0 0 0
1209 3 0 0 0 0 0 0 0 0
1210 3 0 0 0 0 0 0 0 0
1213 9 0 0 3 0 0 0 0 0
1216 27 1 1 15 0 0 0 0 0
fn=_IO_file_xsputn@@GLIBC_2.2.5
1220 8988 1 1 0 0 0 7704 1 0
1226 4926 0 0 0 0 0 0 0 0
1227 1284 0 0 0 0 0 0 0 0
1233 3930 0 0 1572 1 1 0 0 0
1235 1570 0 0 785 0 0 0 0 0
1236 1570 0 0 0 0 0 0 0 0
1239 6838 1 1 0 0 0 0 0 0
1241 5559 0 0 1853 1 1 0 0 0
1250 6 1 1 1 0 0 0 0 0
1254 1570 0 0 0 0 0 0 0 0
1258 2349 0 0 0 0 0 1566 0 0
1259 783 0 0 0 0 0 0 0 0
1260 3132 0 0 0 0 0 0 0 0
1262 1566 0 0 0 0 0 0 0 0
1266 18 1 1 6 1 0 3 0 0
1272 6 0 0 6 0 0 0 0 0
1273 21 0 0 0 0 0 0 0 0
1275 6 0 0 0 0 0 0 0 0
1280 1566 0 0 0 0 0 0 0 0
1286 9 0 0 0 0 0 0 0 0
1287 21 1 1 0 0 0 3 0 0
1290 11556 1 1 8988 1 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/genops.c
fn=_IO_cleanup
849 7 2 2 1 0 0 2 0 0
850 13 2 2 5 0 0 2 0 0
853 12 1 1 4 0 0 0 0 0
862 9 0 0 3 0 0 0 0 0
864 6 1 1 2 0 0 0 0 0
870 16 1 1 5 0 0 2 0 0
878 5 1 1 2 0 0 0 0 0
880 2 0 0 0 0 0 1 0 0
882 2 0 0 1 0 0 1 0 0
883 1 0 0 0 0 0 1 0 0
884 3 0 0 1 0 0 1 0 0
887 5 1 1 2 0 0 1 0 0
889 3 0 0 1 0 0 0 0 0
893 5 0 0 1 0 0 0 0 0
894 9 2 2 4 0 0 1 0 0
901 3 0 0 0 0 0 3 0 0
905 9 0 0 2 0 0 2 0 0
906 2 1 1 0 0 0 0 0 0
926 10 2 2 1 0 0 7 0 0
929 3 0 0 0 0 0 2 0 0
941 12 0 0 10 0 0 0 0 0
fn=_IO_default_setbuf
348 4 0 0 0 0 0 0 0 0
350 1 0 0 0 0 0 1 0 0
351 1 0 0 0 0 0 1 0 0
355 3 0 0 0 0 0 1 0 0
479 8 1 1 0 0 0 4 0 0
480 6 0 0 3 0 0 1 0 0
482 3 1 1 1 0 0 0 0 0
484 2 1 1 0 0 0 1 0 0
485 2 1 1 0 0 0 0 0 0
489 1 0 0 0 0 0 0 0 0
492 3 0 0 0 0 0 3 0 0
493 3 0 0 0 0 0 3 0 0
494 1 0 0 0 0 0 0 0 0
495 6 0 0 5 0 0 0 0 0
fn=_IO_default_xsputn
389 33 1 1 0 0 0 18 0 0
392 6 1 1 0 0 0 0 0 0
393 3 0 0 0 0 0 0 0 0
397 56 1 1 28 0 0 0 0 0
417 105 0 0 33 2 0 11 0 0
419 22 0 0 0 0 0 0 0 0
422 24 1 1 21 0 0 0 0 0
fn=_IO_doallocbuf
361 3 0 0 0 0 0 3 0 0
362 2 1 1 1 0 0 0 0 0
364 4 0 0 1 0 0 0 0 0
365 5 1 1 2 1 0 1 0 0
368 4 0 0 4 0 0 0 0 0
fn=_IO_flush_all_lockp
749 11 2 2 1 0 0 7 0 0
750 1 0 0 0 0 0 0 0 0
754 8 0 0 1 0 0 3 0 0
755 13 2 2 5 1 1 2 0 0
758 12 1 1 4 3 1 0 0 0
760 3 0 0 0 0 0 3 0 0
761 6 1 1 0 0 0 0 0 0
762 1 0 0 1 0 0 0 0 0
764 21 2 2 10 3 2 0 0 0
769 4 0 0 2 0 0 1 0 0
770 3 0 0 0 0 0 0 0 0
772 6 1 1 0 0 0 0 0 0
774 3 0 0 0 0 0 3 0 0
778 9 1 1 2 0 0 2 0 0
779 3 0 0 1 0 0 0 0 0
783 12 1 1 9 0 0 0 0 0
fn=_IO_setb
347 3 1 1 0 0 0 1 0 0
348 4 1 1 2 2 0 0 0 0
350 1 0 0 0 0 0 1 0 0
351 1 0 0 0 0 0 1 0 0
353 6 0 0 0 0 0 1 0 0
356 3 0 0 2 0 0 0 0 0
fn=__overflow
217 398 1 1 0 0 0 199 0 0
219 597 0 0 199 0 0 0 0 0
221 597 0 0 398 0 0 0 0 0
222 398 0 0 199 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/iopadn.c
fn=_IO_padn
37 2256 1 1 188 0 0 1316 0 0
41 376 1 1 0 0 0 0 0 0
44 376 0 0 0 0 0 0 0 0
45 188 0 0 0 0 0 0 0 0
54 564 1 1 0 0 0 0 0 0
62 376 0 0 0 0 0 0 0 0
64 940 0 0 376 1 0 188 0 0
65 188 0 0 0 0 0 0 0 0
68 2256 1 1 1692 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/libioP.h
fn=_IO_cleanup
870 5 0 0 1 0 0 0 0 0
872 2 0 0 0 0 0 0 0 0
873 2 0 0 0 0 0 0 0 0
fn=_IO_default_setbuf
870 3 1 1 0 0 0 0 0 0
872 2 0 0 0 0 0 0 0 0
873 2 0 0 0 0 0 0 0 0
fn=_IO_default_xsputn
870 12 0 0 0 0 0 0 0 0
872 22 0 0 0 0 0 0 0 0
873 22 0 0 0 0 0 0 0 0
fn=_IO_do_write@@GLIBC_2.2.5
873 6 1 1 0 0 0 0 0 0
fn=_IO_doallocbuf
870 3 0 0 0 0 0 0 0 0
872 2 0 0 0 0 0 0 0 0
873 2 1 1 0 0 0 0 0 0
fn=_IO_file_doallocate
870 3 0 0 0 0 0 0 0 0
872 2 0 0 0 0 0 0 0 0
873 2 0 0 0 0 0 0 0 0
fn=_IO_file_xsputn@@GLIBC_2.2.5
870 9 0 0 0 0 0 0 0 0
872 6 0 0 0 0 0 0 0 0
873 6 0 0 0 0 0 0 0 0
fn=_IO_flush_all_lockp
870 4 1 1 0 0 0 0 0 0
872 2 0 0 0 0 0 0 0 0
873 2 0 0 0 0 0 0 0 0
fn=_IO_padn
870 564 1 1 0 0 0 0 0 0
872 376 0 0 0 0 0 0 0 0
873 376 0 0 0 0 0 0 0 0
fn=__overflow
870 597 1 1 0 0 0 0 0 0
872 398 0 0 0 0 0 0 0 0
873 398 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/libio/vtables.c
fn=check_stdfiles_vtables
84 4 2 2 2 1 0 0 0 0
85 3 0 0 2 1 0 0 0 0
86 3 1 1 2 1 0 0 0 0
88 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/malloc/arena.c
fn=malloc_hook_ini
291 3 0 0 1 1 1 0 0 0
fn=ptmalloc_init.part.0
289 5 2 2 1 0 0 2 0 0
294 1 0 0 0 0 0 1 0 0
302 2 0 0 1 0 0 0 0 0
303 7 1 1 0 0 0 1 1 0
304 4 0 0 2 0 0 0 0 0
308 13 2 2 6 2 1 2 1 0
313 7 1 1 1 0 0 2 0 0
314 4 0 0 0 0 0 1 0 0
315 4 0 0 0 0 0 1 0 0
316 4 1 1 0 0 0 1 0 0
317 4 0 0 0 0 0 1 0 0
318 4 0 0 0 0 0 1 0 0
319 4 1 1 0 0 0 1 0 0
320 4 0 0 0 0 0 1 0 0
322 4 0 0 0 0 0 1 0 0
323 4 1 1 0 0 0 1 0 0
324 4 0 0 0 0 0 1 0 0
395 2 0 0 2 2 0 0 0 0
396 2 0 0 0 0 0 0 0 0
399 1 0 0 0 0 0 1 1 0
400 6 0 0 4 0 0 0 0 0
fn=sysmalloc
535 2 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/malloc/hooks.c
fn=malloc_hook_ini
29 5 1 1 0 0 0 2 0 0
30 2 0 0 1 0 0 1 0 0
33 7 1 1 4 2 0 1 1 0
fl=/build/glibc-S9d2JN/glibc-2.27/malloc/malloc.c
fn=_int_malloc
1887 6 1 1 2 1 1 0 0 0
3531 14 1 1 0 0 0 12 0 0
3563 20 1 1 0 0 0 0 0 0
3567 12 0 0 0 0 0 2 0 0
3591 4 0 0 2 0 0 0 0 0
3649 5 1 1 0 0 0 0 0 0
3651 13 1 1 0 0 0 5 0 0
3652 4 1 1 0 0 0 0 0 0
3654 3 0 0 1 0 0 0 0 0
3711 31 2 2 0 0 0 10 0 0
3712 3 0 0 1 0 0 0 0 0
3713 20 2 2 0 0 0 5 0 0
3730 8 2 2 1 0 0 2 0 0
3731 6 0 0 0 0 0 0 0 0
3732 8 1 1 4 0 0 0 0 0
3736 6 0 0 0 0 0 4 0 0
3741 2 0 0 0 0 0 0 0 0
3742 6 0 0 0 0 0 0 0 0
3762 8 0 0 0 0 0 4 0 0
3802 6 1 1 4 1 0 2 0 0
3889 2 0 0 2 0 0 0 0 0
3903 4 2 2 0 0 0 0 0 0
3914 4 1 1 0 0 0 0 0 0
3916 5 0 0 1 0 0 0 0 0
3919 3 0 0 1 0 0 0 0 0
3987 4 1 1 2 0 0 0 0 0
3988 4 0 0 0 0 0 0 0 0
3989 4 0 0 0 0 0 0 0 0
3990 4 0 0 2 0 0 0 0 0
3991 4 0 0 0 0 0 0 0 0
3996 4 0 0 0 0 0 0 0 0
4000 14 1 1 0 0 0 0 0 0
4003 12 1 1 3 0 0 0 0 0
4100 2 0 0 2 0 0 0 0 0
4101 4 0 0 2 0 0 0 0 0
4103 7 1 1 0 0 0 1 0 0
4105 2 1 1 0 0 0 0 0 0
4106 1 0 0 0 0 0 0 0 0
4107 1 0 0 0 0 0 1 0 0
4108 9 1 1 0 0 0 1 0 0
4110 3 0 0 0 0 0 1 1 1
4113 1 0 0 0 0 0 0 0 0
4120 3 0 0 1 0 0 0 0 0
4135 4 1 1 0 0 0 1 0 0
4136 2 1 1 0 0 0 0 0 0
4141 18 1 1 14 0 0 0 0 0
fn=malloc
3038 3 1 1 0 0 0 2 0 0
3043 2 0 0 2 1 0 0 0 0
3044 2 0 0 0 0 0 0 0 0
3045 2 1 1 1 0 0 0 0 0
3091 3 0 0 2 0 0 0 0 0
fn=malloc_hook_ini
2993 5 1 1 2 1 0 2 0 0
3044 2 0 0 0 0 0 0 0 0
3049 11 2 2 0 0 0 0 0 0
3050 2 0 0 0 0 0 0 0 0
3052 4 1 1 2 1 0 0 0 0
3055 3 0 0 2 0 0 0 0 0
3057 5 0 0 1 0 0 0 0 0
3058 3 0 0 1 0 0 0 0 0
3065 4 0 0 1 0 0 0 0 0
3067 4 0 0 0 0 0 1 0 0
3068 7 1 1 1 0 0 0 0 0
fn=ptmalloc_init.part.0
1816 498 1 1 0 0 0 0 0 0
1817 384 2 2 2 0 0 129 33 32
1825 1 0 0 0 0 0 1 1 1
1826 1 0 0 0 0 0 1 1 1
1828 2 0 0 0 0 0 1 0 0
fn=sysmalloc
2274 8 1 1 0 0 0 6 0 0
2294 2 0 0 2 0 0 0 0 0
2305 2 1 1 0 0 0 0 0 0
2306 4 0 0 1 1 1 0 0 0
2321 4 0 0 0 0 0 1 0 0
2387 1 0 0 1 0 0 0 0 0
2388 3 0 0 1 0 0 0 0 0
2389 1 1 1 0 0 0 0 0 0
2398 4 0 0 0 0 0 0 0 0
2404 4 1 1 0 0 0 1 0 0
2407 3 0 0 0 0 0 0 0 0
2460 3 1 1 1 0 0 0 0 0
2468 2 1 1 1 0 0 0 0 0
2469 1 1 1 0 0 0 0 0 0
2479 6 0 0 0 0 0 2 0 0
2487 2 0 0 0 0 0 0 0 0
2489 5 0 0 2 2 0 2 0 0
2490 1 0 0 0 0 0 0 0 0
2493 3 0 0 1 0 0 0 0 0
2496 4 1 1 2 1 0 0 0 0
2497 2 0 0 0 0 0 0 0 0
2541 3 1 1 0 0 0 0 0 0
2543 2 0 0 1 0 0 0 0 0
2544 2 1 1 0 0 0 1 0 0
2545 3 0 0 1 0 0 1 0 0
2551 2 0 0 0 0 0 0 0 0
2554 4 2 2 1 0 0 0 0 0
2588 2 0 0 0 0 0 0 0 0
2594 3 0 0 0 0 0 0 0 0
2616 2 1 1 0 0 0 0 0 0
2617 6 0 0 1 0 0 0 0 0
2619 2 0 0 0 0 0 0 0 0
2620 4 0 0 2 0 0 2 0 0
2632 3 1 1 1 0 0 0 0 0
2640 2 1 1 2 0 0 0 0 0
2641 4 0 0 1 0 0 0 0 0
2679 1 0 0 0 0 0 1 0 0
2680 4 0 0 0 0 0 1 1 1
2681 2 0 0 0 0 0 1 0 0
2692 2 1 1 0 0 0 0 0 0
2724 2 1 1 1 0 0 0 0 0
2725 1 0 0 0 0 0 1 0 0
2730 2 0 0 1 0 0 0 0 0
2733 2 1 1 1 0 0 0 0 0
2735 1 0 0 0 0 0 0 0 0
2736 1 0 0 0 0 0 0 0 0
2737 1 0 0 0 0 0 1 0 0
2738 8 0 0 0 0 0 1 0 0
2739 2 0 0 0 0 0 1 1 1
2741 2 1 1 0 0 0 0 0 0
2747 9 1 1 7 0 0 0 0 0
fn=tcache_init.part.4
2987 1 0 0 0 0 0 1 0 0
2996 10 2 2 4 1 0 0 0 0
2997 4 1 1 0 0 0 1 0 0
2998 2 0 0 0 0 0 0 0 0
3006 4 0 0 2 0 0 0 0 0
3013 2 0 0 0 0 0 0 0 0
3015 2 1 1 1 0 0 1 0 0
3016 80 0 0 0 0 0 73 8 8
3019 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/malloc/morecore.c
fn=__default_morecore
46 2 1 1 0 0 0 0 0 0
47 2 0 0 0 0 0 2 0 0
49 6 0 0 0 0 0 0 0 0
52 4 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/misc/../sysdeps/unix/syscall-template.S
fn=mprotect
78 24 0 0 0 0 0 0 0 0
79 6 0 0 6 0 0 0 0 0
fn=munmap
78 4 1 1 0 0 0 0 0 0
79 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/misc/../sysdeps/unix/sysv/linux/mmap64.c
fn=mmap
48 84 1 1 0 0 0 42 1 1
51 14 1 1 0 0 0 0 0 0
54 26 1 1 2 0 0 0 0 0
59 70 0 0 0 0 0 0 0 0
61 49 0 0 49 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/misc/../sysdeps/unix/sysv/linux/x86_64/brk.c
fn=brk
31 16 2 2 2 0 0 2 0 0
33 4 0 0 0 0 0 0 0 0
39 2 0 0 0 0 0 0 0 0
40 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/misc/init-misc.c
fn=__init_misc
30 3 0 0 0 0 0 2 0 0
31 6 1 1 1 0 0 0 0 0
33 3 0 0 0 0 0 1 0 0
37 5 0 0 1 1 0 1 0 0
38 3 1 1 2 0 0 1 0 0
40 4 0 0 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/misc/sbrk.c
fn=sbrk
32 8 1 1 0 0 0 6 0 0
40 11 0 0 5 3 0 0 0 0
41 5 1 1 1 0 0 1 0 0
44 4 0 0 0 0 0 0 0 0
48 6 0 0 0 0 0 0 0 0
56 4 1 1 0 0 0 1 0 0
60 10 0 0 8 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/nptl/unregister-atfork.c
fn=__unregister_atfork
28 14 1 1 2 0 0 6 0 0
36 2 0 0 2 0 0 0 0 0
39 4 1 1 0 0 0 0 0 0
121 12 0 0 10 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/posix/../sysdeps/unix/syscall-template.S
fn=uname
78 4 1 1 0 0 0 0 0 0
79 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/posix/../sysdeps/unix/sysv/linux/_exit.c
fn=_Exit
27 2 1 1 1 0 0 0 0 0
31 4 1 1 0 0 0 0 0 0
33 2 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/setjmp/../sysdeps/x86_64/bsd-_setjmp.S
fn=_setjmp
30 1 1 1 0 0 0 0 0 0
32 1 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/setjmp/../sysdeps/x86_64/setjmp.S
fn=__sigsetjmp
26 4 2 2 0 0 0 4 0 0
35 4 0 0 0 0 0 0 0 0
36 8 1 1 4 0 0 0 0 0
37 4 0 0 0 0 0 4 0 0
41 4 0 0 0 0 0 4 1 1
42 4 0 0 0 0 0 4 0 0
43 4 0 0 0 0 0 4 0 0
44 4 0 0 0 0 0 4 0 0
45 4 0 0 0 0 0 0 0 0
47 8 1 1 4 0 0 0 0 0
49 4 0 0 0 0 0 4 0 0
50 4 0 0 4 0 0 0 0 0
51 4 0 0 0 0 0 0 0 0
53 8 0 0 4 0 0 0 0 0
55 4 0 0 0 0 0 4 0 0
59 3 0 0 0 0 0 0 0 0
60 3 0 0 3 0 0 0 0 0
63 1 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/setjmp/sigjmp.c
fn=__sigjmp_save
28 2 0 0 0 0 0 1 0 0
29 3 0 0 0 0 0 1 0 0
34 3 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdio-common/../libio/libioP.h
fn=vfprintf
870 1495 1 1 0 0 0 299 0 0
872 2989 1 1 0 0 0 0 0 0
873 2192 0 0 797 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdio-common/_itoa.c
fn=_itoa_word
168 1196 2 2 0 0 0 0 0 0
170 598 0 0 0 0 0 0 0 0
179 8650 1 1 671 1 1 671 1 0
188 598 0 0 299 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdio-common/printf-parse.h
fn=vfprintf
73 398 1 1 199 0 0 0 0 0
75 1393 0 0 398 0 0 0 0 0
85 199 0 0 0 0 0 0 0 0
108 3686 0 0 0 0 0 1594 1 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdio-common/printf.c
fn=printf
28 3289 3 3 299 0 0 1794 3 2
32 1794 1 1 0 0 0 1196 1 0
33 1495 0 0 598 1 0 299 0 0
37 1495 0 0 897 1 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdio-common/vfprintf.c
fn=vfprintf
1244 4186 1 1 299 0 0 2093 1 0
1246 598 1 1 0 0 0 598 1 0
1275 897 1 1 598 0 0 299 1 0
1279 299 0 0 0 0 0 299 1 0
1283 1494 0 0 299 0 0 1 0 0
1287 1495 0 0 299 0 0 0 0 0
1298 1196 1 1 0 0 0 299 0 0
1305 299 0 0 0 0 0 299 0 0
1309 1196 0 0 598 0 0 598 4 0
1313 299 0 0 0 0 0 299 0 0
1324 3289 2 2 598 0 0 1196 2 0
1325 3887 2 2 2093 1 1 299 0 0
1328 3289 1 1 897 1 0 299 0 0
1332 897 0 0 598 1 0 0 0 0
1336 2392 1 1 897 3 0 0 0 0
1357 498 0 0 0 0 0 498 0 0
1358 498 0 0 0 0 0 498 0 0
1359 498 0 0 0 0 0 498 0 0
1360 498 0 0 0 0 0 498 0 0
1361 498 1 1 0 0 0 498 0 0
1362 498 0 0 0 0 0 0 0 0
1363 498 0 0 0 0 0 498 0 0
1364 498 0 0 0 0 0 0 0 0
1365 498 0 0 0 0 0 498 0 0
1366 498 0 0 0 0 0 0 0 0
1367 498 0 0 0 0 0 0 0 0
1370 498 0 0 0 0 0 498 0 0
1371 498 0 0 0 0 0 498 0 0
1374 996 0 0 0 0 0 498 0 0
1375 1494 1 1 498 0 0 498 0 0
1378 7470 1 1 1494 2 2 0 0 0
1498 597 2 2 0 0 0 199 0 0
1506 398 0 0 0 0 0 0 0 0
1523 398 1 1 0 0 0 0 0 0
1526 2786 1 1 398 2 2 0 0 0
1642 42852 32 32 12600 2 0 5413 0 0
1643 870 1 1 580 0 0 0 0 0
1660 498 1 1 498 0 0 0 0 0
1662 996 1 1 498 0 0 0 0 0
1670 498 0 0 0 0 0 0 0 0
1674 9462 1 1 1494 0 0 996 0 0
1676 1793 0 0 996 0 0 0 0 0
1696 3289 2 2 1495 1 0 299 0 0
1697 897 0 0 299 0 0 0 0 0
1700 3588 1 1 2691 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdlib/cxa_atexit.c
fn=__cxa_atexit
39 7 1 1 2 2 2 0 0 0
40 2 0 0 0 0 0 1 0 0
42 2 0 0 0 0 0 0 0 0
49 2 0 0 1 0 0 0 0 0
51 1 1 1 0 0 0 1 0 0
52 1 0 0 0 0 0 1 0 0
53 1 0 0 0 0 0 1 0 0
54 1 0 0 0 0 0 1 0 0
55 4 0 0 2 0 0 0 0 0
56 1 0 0 0 0 0 0 0 0
65 8 1 1 0 0 0 4 0 0
67 6 1 1 5 0 0 0 0 0
fn=__new_exitfn
78 3 0 0 0 0 0 2 0 0
79 2 0 0 0 0 0 0 0 0
84 2 1 1 1 1 0 0 0 0
89 8 1 1 2 1 0 0 0 0
91 3 0 0 1 1 0 0 0 0
99 2 1 1 0 0 0 1 0 0
120 1 1 1 0 0 0 0 0 0
121 2 0 0 0 0 0 1 0 0
134 1 0 0 0 0 0 1 0 0
135 1 0 0 1 0 0 0 0 0
139 4 0 0 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdlib/cxa_finalize.c
fn=__cxa_finalize
30 16 1 1 0 0 0 12 0 0
33 14 0 0 4 0 0 0 0 0
36 12 2 2 4 0 0 0 0 0
40 14 0 0 2 0 0 0 0 0
94 16 2 2 4 0 0 0 0 0
98 12 0 0 2 1 1 0 0 0
106 4 0 0 0 0 0 0 0 0
107 4 0 0 0 0 0 2 0 0
109 8 0 0 4 0 0 0 0 0
110 16 1 1 14 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdlib/cxa_thread_atexit_impl.c
fn=__call_tls_dtors
145 3 1 1 0 0 0 2 0 0
146 4 0 0 2 0 0 0 0 0
164 4 1 1 3 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/stdlib/exit.c
fn=__run_exit_handlers
40 10 2 2 0 0 0 7 0 0
45 3 0 0 0 0 0 0 0 0
46 2 1 1 0 0 0 1 0 0
53 1 0 0 0 0 0 0 0 0
56 14 0 0 4 0 0 0 0 0
59 2 1 1 2 1 0 0 0 0
61 5 0 0 0 0 0 0 0 0
65 1 0 0 0 0 0 1 1 0
66 4 1 1 2 0 0 0 0 0
70 6 1 1 2 1 0 0 0 0
72 2 0 0 0 0 0 1 0 0
73 1 0 0 1 0 0 0 0 0
76 4 0 0 2 0 0 0 0 0
77 8 1 1 1 0 0 0 0 0
103 1 0 0 0 0 0 1 0 0
106 3 1 1 2 0 0 0 0 0
108 3 0 0 1 0 0 1 0 0
109 1 0 0 0 0 0 0 0 0
112 6 1 1 2 0 0 0 0 0
114 2 0 0 1 0 0 0 0 0
120 2 0 0 1 0 0 1 0 0
121 2 0 0 0 0 0 0 0 0
126 4 1 1 2 0 0 0 0 0
129 2 0 0 1 0 0 0 0 0
130 14 0 0 1 1 0 1 0 0
132 2 0 0 0 0 0 1 0 0
fn=exit
138 1 0 0 0 0 0 0 0 0
139 4 1 1 0 0 0 1 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../bits/stdlib-bsearch.h
fn=intel_check_word.isra.0
27 24 0 0 0 0 0 0 0 0
28 12 1 1 0 0 0 0 0 0
29 288 0 0 0 0 0 0 0 0
31 162 0 0 0 0 0 0 0 0
32 81 0 0 0 0 0 0 0 0
37 15 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86/cacheinfo.c
fn=handle_intel.constprop.1
259 30 2 2 3 0 0 21 0 0
261 3 0 0 3 0 0 0 0 0
264 9 0 0 3 0 0 0 0 0
270 3 0 0 0 0 0 3 0 0
272 3 0 0 0 0 0 3 0 0
273 3 0 0 0 0 0 3 0 0
275 12 0 0 0 0 0 0 0 0
281 15 1 1 0 0 0 6 0 0
286 6 0 0 0 0 0 0 0 0
288 6 0 0 0 0 0 3 0 0
289 3 0 0 0 0 0 0 0 0
293 18 0 0 0 0 0 3 0 0
295 6 1 1 0 0 0 0 0 0
298 21 0 0 0 0 0 3 0 0
300 6 0 0 0 0 0 0 0 0
319 33 1 1 27 0 0 0 0 0
fn=init_cacheinfo
488 7 0 0 0 0 0 6 0 0
500 2 1 1 1 0 0 1 0 0
502 6 1 1 4 0 0 0 0 0
504 3 0 0 0 0 0 1 0 0
506 3 0 0 0 0 0 2 0 0
510 1 0 0 0 0 0 1 0 0
511 3 0 0 0 0 0 1 0 0
519 2 1 1 0 0 0 0 0 0
530 1 0 0 0 0 0 0 0 0
535 3 0 0 1 0 0 0 0 0
539 2 0 0 1 0 0 0 0 0
547 9 1 1 0 0 0 0 0 0
550 14 0 0 0 0 0 0 0 0
556 8 1 1 0 0 0 0 0 0
559 26 0 0 0 0 0 0 0 0
564 2 0 0 0 0 0 0 0 0
568 4 0 0 0 0 0 0 0 0
569 1 0 0 0 0 0 0 0 0
573 2 0 0 0 0 0 0 0 0
577 3 0 0 0 0 0 0 0 0
580 3 0 0 0 0 0 0 0 0
581 1 0 0 0 0 0 0 0 0
586 8 0 0 0 0 0 0 0 0
592 2 1 1 1 0 0 0 0 0
600 8 0 0 1 0 0 0 0 0
602 7 1 1 0 0 0 0 0 0
604 7 0 0 0 0 0 0 0 0
606 6 0 0 0 0 0 0 0 0
609 2 0 0 0 0 0 0 0 0
610 8 1 1 0 0 0 0 0 0
612 4 0 0 0 0 0 0 0 0
615 2 0 0 0 0 0 0 0 0
620 1 0 0 0 0 0 0 0 0
622 4 0 0 0 0 0 0 0 0
623 3 0 0 0 0 0 0 0 0
624 1 0 0 0 0 0 0 0 0
627 2 0 0 0 0 0 0 0 0
630 3 1 1 0 0 0 0 0 0
634 2 1 1 1 0 0 0 0 0
637 1 0 0 0 0 0 0 0 0
639 4 0 0 0 0 0 0 0 0
640 1 0 0 0 0 0 0 0 0
645 2 0 0 0 0 0 0 0 0
650 2 0 0 0 0 0 0 0 0
651 1 0 0 0 0 0 0 0 0
652 2 1 1 0 0 0 0 0 0
653 1 0 0 0 0 0 0 0 0
654 2 0 0 1 0 0 0 0 0
691 4 1 1 0 0 0 0 0 0
692 5 0 0 0 0 0 0 0 0
696 2 0 0 0 0 0 0 0 0
755 2 1 1 0 0 0 0 0 0
758 2 0 0 0 0 0 0 0 0
760 3 1 1 0 0 0 1 0 0
761 1 0 0 0 0 0 1 1 1
763 1 0 0 0 0 0 0 0 0
764 3 0 0 0 0 0 1 0 0
765 1 0 0 0 0 0 1 0 0
768 2 0 0 0 0 0 0 0 0
771 2 0 0 0 0 0 0 0 0
773 3 0 0 0 0 0 1 0 0
774 1 0 0 0 0 0 1 1 1
776 1 0 0 0 0 0 0 0 0
777 3 1 1 0 0 0 1 0 0
778 1 0 0 0 0 0 1 0 0
786 2 0 0 1 0 0 1 1 1
788 8 0 0 1 0 0 0 0 0
789 8 0 0 7 0 0 0 0 0
fn=intel_check_word.isra.0
119 162 0 0 81 6 6 0 0 0
122 81 0 0 0 0 0 0 0 0
128 36 0 0 0 0 0 24 0 0
132 12 1 1 0 0 0 0 0 0
134 3 1 1 0 0 0 0 0 0
138 42 1 1 0 0 0 0 0 0
140 48 0 0 0 0 0 0 0 0
142 15 1 1 0 0 0 0 0 0
144 30 0 0 0 0 0 0 0 0
152 30 0 0 0 0 0 0 0 0
161 13 0 0 0 0 0 0 0 0
164 30 2 2 0 0 0 0 0 0
167 24 0 0 0 0 0 0 0 0
171 16 2 2 0 0 0 0 0 0
173 36 0 0 0 0 0 0 0 0
175 14 0 0 0 0 0 0 0 0
177 8 0 0 0 0 0 0 0 0
178 14 0 0 0 0 0 0 0 0
179 10 0 0 0 0 0 0 0 0
181 3 1 1 0 0 0 0 0 0
183 6 0 0 0 0 0 0 0 0
185 9 1 1 0 0 0 0 0 0
186 12 0 0 0 0 0 0 0 0
187 9 0 0 0 0 0 0 0 0
188 15 0 0 0 0 0 0 0 0
196 5 0 0 0 0 0 0 0 0
203 24 0 0 0 0 0 0 0 0
225 12 0 0 0 0 0 0 0 0
250 12 0 0 0 0 0 0 0 0
255 36 0 0 30 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/memcmp.S
fn=bcmp
28 4 1 1 0 0 0 0 0 0
29 4 0 0 0 0 0 0 0 0
30 4 0 0 0 0 0 0 0 0
31 4 0 0 0 0 0 0 0 0
32 4 0 0 0 0 0 0 0 0
33 4 0 0 0 0 0 0 0 0
34 4 0 0 0 0 0 0 0 0
35 4 0 0 0 0 0 0 0 0
38 4 0 0 0 0 0 0 0 0
39 4 0 0 0 0 0 0 0 0
40 3 0 0 3 0 0 0 0 0
41 3 0 0 3 2 2 0 0 0
42 3 0 0 0 0 0 0 0 0
43 3 0 0 0 0 0 0 0 0
44 3 1 1 0 0 0 0 0 0
45 3 0 0 0 0 0 0 0 0
46 3 0 0 0 0 0 0 0 0
48 2 0 0 0 0 0 0 0 0
49 2 0 0 0 0 0 0 0 0
50 1 0 0 1 0 0 0 0 0
51 1 0 0 1 0 0 0 0 0
52 1 0 0 0 0 0 0 0 0
53 1 0 0 0 0 0 0 0 0
54 1 0 0 0 0 0 0 0 0
55 1 0 0 0 0 0 0 0 0
56 1 0 0 0 0 0 0 0 0
58 2 0 0 0 0 0 0 0 0
59 2 0 0 0 0 0 0 0 0
60 2 0 0 2 0 0 0 0 0
61 2 0 0 2 1 1 0 0 0
62 2 0 0 0 0 0 0 0 0
63 2 0 0 0 0 0 0 0 0
64 1 0 0 0 0 0 0 0 0
65 1 1 1 0 0 0 0 0 0
66 1 0 0 0 0 0 0 0 0
68 1 0 0 0 0 0 0 0 0
69 1 0 0 0 0 0 0 0 0
70 1 0 0 1 0 0 0 0 0
71 1 0 0 1 0 0 0 0 0
72 1 0 0 0 0 0 0 0 0
73 1 0 0 0 0 0 0 0 0
98 2 1 1 2 0 0 0 0 0
102 2 0 0 0 0 0 0 0 0
103 2 0 0 0 0 0 0 0 0
118 2 1 1 0 0 0 0 0 0
119 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/../strchr.S
fn=index
24 6 1 1 0 0 0 0 0 0
25 6 0 0 0 0 0 0 0 0
26 6 0 0 0 0 0 0 0 0
27 6 0 0 0 0 0 0 0 0
28 6 0 0 0 0 0 0 0 0
29 6 0 0 0 0 0 0 0 0
30 6 0 0 0 0 0 0 0 0
31 6 0 0 0 0 0 0 0 0
32 6 0 0 6 2 2 0 0 0
33 6 0 0 0 0 0 0 0 0
34 6 0 0 0 0 0 0 0 0
35 6 0 0 0 0 0 0 0 0
36 6 0 0 0 0 0 0 0 0
37 6 0 0 0 0 0 0 0 0
38 6 0 0 0 0 0 0 0 0
39 6 1 1 0 0 0 0 0 0
40 6 0 0 0 0 0 0 0 0
41 4 0 0 0 0 0 0 0 0
45 4 0 0 0 0 0 0 0 0
46 4 0 0 0 0 0 0 0 0
47 4 0 0 4 0 0 0 0 0
48 4 0 0 0 0 0 0 0 0
50 4 0 0 4 0 0 0 0 0
54 2 0 0 2 0 0 0 0 0
55 2 0 0 0 0 0 0 0 0
56 2 0 0 0 0 0 0 0 0
57 2 0 0 0 0 0 0 0 0
58 2 0 0 0 0 0 0 0 0
59 2 0 0 0 0 0 0 0 0
60 2 0 0 2 1 1 0 0 0
61 2 0 0 0 0 0 0 0 0
62 2 0 0 0 0 0 0 0 0
63 2 1 1 0 0 0 0 0 0
64 2 0 0 0 0 0 0 0 0
65 2 0 0 0 0 0 0 0 0
66 2 0 0 0 0 0 0 0 0
67 2 0 0 2 0 0 0 0 0
68 2 0 0 0 0 0 0 0 0
69 2 0 0 0 0 0 0 0 0
70 2 0 0 0 0 0 0 0 0
71 2 0 0 0 0 0 0 0 0
72 2 0 0 0 0 0 0 0 0
73 2 0 0 0 0 0 0 0 0
74 2 0 0 0 0 0 0 0 0
75 2 0 0 0 0 0 0 0 0
76 2 0 0 0 0 0 0 0 0
77 2 0 0 0 0 0 0 0 0
129 2 1 1 0 0 0 0 0 0
133 2 0 0 0 0 0 0 0 0
134 2 0 0 0 0 0 0 0 0
135 2 0 0 2 0 0 0 0 0
136 2 0 0 0 0 0 0 0 0
138 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/../strlen.S
fn=strlen
79 14 1 1 0 0 0 0 0 0
80 14 0 0 0 0 0 0 0 0
81 14 0 0 0 0 0 0 0 0
82 14 0 0 0 0 0 0 0 0
83 14 0 0 0 0 0 0 0 0
84 14 0 0 0 0 0 0 0 0
85 14 0 0 0 0 0 0 0 0
87 14 1 1 0 0 0 0 0 0
89 14 0 0 0 0 0 0 0 0
120 14 0 0 14 3 3 0 0 0
121 14 0 0 0 0 0 0 0 0
122 14 0 0 0 0 0 0 0 0
123 14 0 0 0 0 0 0 0 0
124 14 0 0 0 0 0 0 0 0
125 8 0 0 0 0 0 0 0 0
127 8 0 0 8 0 0 0 0 0
131 6 0 0 0 0 0 0 0 0
132 6 0 0 6 0 0 0 0 0
133 6 0 0 6 0 0 0 0 0
134 6 0 0 6 1 1 0 0 0
135 6 0 0 0 0 0 0 0 0
136 6 0 0 0 0 0 0 0 0
137 6 0 0 0 0 0 0 0 0
138 6 0 0 0 0 0 0 0 0
139 6 1 1 0 0 0 0 0 0
140 6 0 0 0 0 0 0 0 0
141 6 0 0 0 0 0 0 0 0
142 6 0 0 0 0 0 0 0 0
147 48 0 0 6 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-avx2.h
fn=memchr
30 4 0 0 0 0 0 0 0 0
32 3 1 1 2 0 0 0 0 0
fn=memrchr
30 4 1 1 0 0 0 0 0 0
32 3 1 1 2 0 0 0 0 0
fn=rawmemchr
30 4 1 1 0 0 0 0 0 0
32 3 1 1 2 0 0 0 0 0
fn=rindex
30 4 0 0 0 0 0 0 0 0
32 3 1 1 2 0 0 0 0 0
fn=strchrnul
30 4 0 0 0 0 0 0 0 0
32 3 0 0 2 0 0 0 0 0
fn=strlen
30 4 0 0 0 0 0 0 0 0
32 3 1 1 2 0 0 0 0 0
fn=strnlen
30 8 1 1 0 0 0 0 0 0
32 6 1 1 4 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-memcmp.h
fn=bcmp
32 2 0 0 0 0 0 0 0 0
33 5 1 1 3 0 0 0 0 0
34 2 0 0 0 0 0 0 0 0
35 3 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-memmove.h
fn=memcpy@@GLIBC_2.14
44 5 1 1 2 0 0 0 0 0
47 2 0 0 0 0 0 0 0 0
48 2 1 1 0 0 0 0 0 0
59 2 0 0 0 0 0 0 0 0
61 5 1 1 2 0 0 0 0 0
fn=memmove
44 10 2 2 4 1 0 0 0 0
47 4 0 0 0 0 0 0 0 0
48 4 0 0 0 0 0 0 0 0
59 4 0 0 0 0 0 0 0 0
61 10 1 1 4 1 0 0 0 0
fn=mempcpy
44 5 1 1 2 0 0 0 0 0
47 2 0 0 0 0 0 0 0 0
48 2 1 1 0 0 0 0 0 0
59 2 0 0 0 0 0 0 0 0
61 5 1 1 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-memset.h
fn=memset
42 5 1 1 2 0 0 0 0 0
45 4 0 0 1 0 0 0 0 0
46 2 0 0 0 0 0 0 0 0
57 2 0 0 0 0 0 0 0 0
59 5 1 1 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-sse4_2.h
fn=strcspn
30 5 2 2 2 0 0 0 0 0
fn=strpbrk
30 5 0 0 2 0 0 0 0 0
fn=strspn
30 5 1 1 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-strcasecmp.h
fn=strcasecmp
32 5 1 1 2 0 0 0 0 0
fn=strcasecmp_l
32 5 1 1 2 0 0 0 0 0
fn=strncasecmp
32 5 0 0 2 0 0 0 0 0
fn=strncasecmp_l
32 5 1 1 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/ifunc-unaligned-ssse3.h
fn=stpcpy
33 4 1 1 2 0 0 0 0 0
fn=stpncpy
33 4 1 1 2 0 0 0 0 0
fn=strcat
33 4 1 1 2 0 0 0 0 0
fn=strcpy
33 4 0 0 2 0 0 0 0 0
fn=strncpy
33 4 1 1 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memchr.c
fn=memchr
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memcmp.c
fn=bcmp
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S
fn=__memcpy_avx_unaligned_erms
227 783 1 1 0 0 0 0 0 0
228 783 0 0 0 0 0 0 0 0
272 783 1 1 0 0 0 0 0 0
273 783 0 0 0 0 0 0 0 0
275 783 0 0 0 0 0 0 0 0
276 783 0 0 0 0 0 0 0 0
277 783 0 0 0 0 0 0 0 0
278 783 0 0 0 0 0 0 0 0
279 586 0 0 0 0 0 0 0 0
280 586 0 0 0 0 0 0 0 0
281 192 0 0 0 0 0 0 0 0
282 192 0 0 192 0 0 0 0 0
283 192 0 0 0 0 0 192 0 0
285 192 0 0 192 0 0 0 0 0
314 197 0 0 197 0 0 0 0 0
315 197 0 0 197 0 0 0 0 0
316 197 0 0 0 0 0 197 15 15
317 197 0 0 0 0 0 197 0 0
318 197 0 0 197 0 0 0 0 0
321 394 1 1 394 0 0 0 0 0
322 394 0 0 394 0 0 0 0 0
323 394 0 0 0 0 0 394 0 0
324 394 1 1 0 0 0 394 0 0
325 394 0 0 394 0 0 0 0 0
fn=__mempcpy_avx_unaligned_erms
208 783 1 1 0 0 0 0 0 0
209 783 0 0 0 0 0 0 0 0
210 783 0 0 0 0 0 0 0 0
fn=memcpy
129 14 1 1 0 0 0 0 0 0
135 40 0 0 0 0 0 0 0 0
136 40 0 0 0 0 0 0 0 0
137 12 0 0 0 0 0 0 0 0
138 12 0 0 0 0 0 0 0 0
143 8 0 0 8 1 0 0 0 0
144 8 0 0 8 0 0 0 0 0
145 8 0 0 0 0 0 8 4 4
146 8 0 0 0 0 0 8 0 0
151 8 0 0 8 0 0 0 0 0
275 28 1 1 0 0 0 0 0 0
276 28 0 0 0 0 0 0 0 0
277 9 0 0 0 0 0 0 0 0
278 9 0 0 0 0 0 0 0 0
279 4 0 0 0 0 0 0 0 0
280 4 0 0 0 0 0 0 0 0
281 2 0 0 0 0 0 0 0 0
282 1 0 0 1 0 0 0 0 0
283 1 0 0 0 0 0 1 1 1
285 2 0 0 2 0 0 0 0 0
307 19 0 0 19 0 0 0 0 0
308 19 0 0 19 0 0 0 0 0
309 19 0 0 0 0 0 19 2 2
310 19 0 0 0 0 0 19 0 0
311 19 0 0 19 0 0 0 0 0
314 5 0 0 5 0 0 0 0 0
315 5 0 0 5 0 0 0 0 0
316 5 0 0 0 0 0 5 0 0
317 5 0 0 0 0 0 5 0 0
318 5 0 0 5 0 0 0 0 0
321 2 1 1 2 1 1 0 0 0
322 2 0 0 2 0 0 0 0 0
323 2 0 0 0 0 0 2 1 1
324 2 0 0 0 0 0 2 0 0
325 2 0 0 2 0 0 0 0 0
335 4 0 0 0 0 0 0 0 0
336 4 0 0 0 0 0 0 0 0
337 4 0 0 0 0 0 0 0 0
338 4 0 0 0 0 0 0 0 0
360 4 1 1 4 0 0 0 0 0
361 4 0 0 4 0 0 0 0 0
362 4 0 0 4 0 0 0 0 0
363 4 0 0 4 0 0 0 0 0
364 4 0 0 0 0 0 4 2 2
365 4 1 1 0 0 0 4 0 0
366 4 0 0 0 0 0 4 3 3
367 4 0 0 0 0 0 4 0 0
369 4 0 0 4 0 0 0 0 0
fn=mempcpy
116 26 0 0 0 0 0 0 0 0
117 26 0 0 0 0 0 0 0 0
118 26 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memrchr.c
fn=memrchr
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/memset-vec-unaligned-erms.S
fn=memset
109 65 2 1 0 0 0 0 0 0
115 13 0 0 0 0 0 0 0 0
116 13 0 0 0 0 0 0 0 0
117 6 0 0 0 0 0 0 0 0
118 6 0 0 0 0 0 0 0 0
120 4 0 0 0 0 0 4 2 2
121 4 0 0 0 0 0 4 0 0
123 4 0 0 4 0 0 0 0 0
182 2 1 1 0 0 0 0 0 0
183 2 0 0 0 0 0 0 0 0
193 2 0 0 0 0 0 0 0 0
194 2 0 0 0 0 0 2 2 2
195 2 0 0 0 0 0 0 0 0
196 2 0 0 0 0 0 2 2 2
197 2 0 0 0 0 0 2 0 0
198 2 0 0 0 0 0 2 0 0
199 2 0 0 0 0 0 2 1 1
200 2 0 0 0 0 0 2 0 0
201 2 0 0 0 0 0 2 0 0
202 2 0 0 0 0 0 2 0 0
203 2 0 0 0 0 0 0 0 0
204 2 0 0 0 0 0 0 0 0
205 2 0 0 0 0 0 0 0 0
206 2 0 0 0 0 0 0 0 0
208 31 0 0 0 0 0 31 28 28
209 31 0 0 0 0 0 31 0 0
210 31 0 0 0 0 0 31 0 0
211 31 0 0 0 0 0 31 0 0
212 31 0 0 0 0 0 0 0 0
213 31 0 0 0 0 0 0 0 0
214 31 0 0 0 0 0 0 0 0
215 2 0 0 2 0 0 0 0 0
230 7 2 1 0 0 0 0 0 0
231 7 0 0 0 0 0 0 0 0
232 7 2 1 0 0 0 0 0 0
233 6 0 0 0 0 0 0 0 0
234 6 0 0 0 0 0 0 0 0
235 2 0 0 0 0 0 0 0 0
236 2 0 0 0 0 0 0 0 0
260 1 0 0 0 0 0 1 1 1
261 1 0 0 0 0 0 1 0 0
263 1 0 0 1 0 0 0 0 0
266 4 0 0 0 0 0 4 0 0
267 4 0 0 0 0 0 4 0 0
269 4 0 0 4 0 0 0 0 0
272 2 0 0 0 0 0 2 0 0
273 2 0 0 0 0 0 2 0 0
275 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/rawmemchr.c
fn=rawmemchr
31 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/stpcpy.c
fn=stpcpy
33 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/stpncpy.c
fn=stpncpy
31 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcasecmp.c
fn=strcasecmp
31 1 1 1 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcasecmp_l.c
fn=strcasecmp_l
31 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcat.c
fn=strcat
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strchr-avx2.S
fn=__strchrnul_avx2
45 797 1 1 0 0 0 0 0 0
47 797 0 0 0 0 0 0 0 0
48 797 0 0 0 0 0 0 0 0
49 797 0 0 0 0 0 0 0 0
51 797 0 0 0 0 0 0 0 0
52 797 0 0 0 0 0 0 0 0
53 797 0 0 0 0 0 0 0 0
57 797 0 0 797 0 0 0 0 0
58 797 0 0 0 0 0 0 0 0
59 797 0 0 0 0 0 0 0 0
60 797 0 0 0 0 0 0 0 0
61 797 0 0 0 0 0 0 0 0
62 797 0 0 0 0 0 0 0 0
63 797 1 1 0 0 0 0 0 0
184 797 1 1 0 0 0 0 0 0
186 797 0 0 0 0 0 0 0 0
193 797 0 0 0 0 0 0 0 0
194 797 0 0 797 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strchr.c
fn=index
38 3 0 0 0 0 0 0 0 0
40 4 1 1 2 0 0 0 0 0
49 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strchrnul.c
fn=strchrnul
31 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcmp.c
fn=strcmp
38 4 1 1 2 0 0 0 0 0
47 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcpy.c
fn=strcpy
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strcspn.c
fn=strcspn
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strlen.c
fn=strlen
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncase.c
fn=strncasecmp
31 1 1 1 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncase_l.c
fn=strncasecmp_l
31 1 1 1 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncmp.c
fn=strncmp
38 4 1 1 2 0 0 0 0 0
39 3 0 0 1 0 0 0 0 0
48 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strncpy.c
fn=strncpy
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strnlen.c
fn=strnlen
31 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strpbrk.c
fn=strpbrk
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strrchr-avx2.S
fn=__strrchr_avx2
43 1 1 1 0 0 0 0 0 0
44 1 0 0 0 0 0 0 0 0
46 1 0 0 0 0 0 0 0 0
47 1 0 0 0 0 0 0 0 0
50 1 0 0 0 0 0 0 0 0
51 1 0 0 0 0 0 0 0 0
52 1 0 0 0 0 0 0 0 0
85 1 1 1 0 0 0 0 0 0
86 1 0 0 0 0 0 0 0 0
87 1 0 0 1 1 0 0 0 0
88 1 0 0 0 0 0 0 0 0
89 1 1 1 0 0 0 0 0 0
90 1 0 0 0 0 0 0 0 0
91 1 0 0 0 0 0 0 0 0
92 1 0 0 0 0 0 0 0 0
93 1 0 0 0 0 0 0 0 0
94 1 0 0 0 0 0 0 0 0
97 1 0 0 0 0 0 0 0 0
98 1 0 0 0 0 0 0 0 0
107 1 0 0 0 0 0 0 0 0
108 1 0 0 0 0 0 0 0 0
207 1 1 1 0 0 0 0 0 0
208 1 0 0 0 0 0 0 0 0
216 1 0 0 0 0 0 0 0 0
217 1 0 0 0 0 0 0 0 0
218 1 0 0 0 0 0 0 0 0
219 1 0 0 0 0 0 0 0 0
220 1 0 0 0 0 0 0 0 0
222 1 0 0 0 0 0 0 0 0
223 1 0 0 0 0 0 0 0 0
224 1 0 0 0 0 0 0 0 0
225 1 0 0 0 0 0 0 0 0
226 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strrchr.c
fn=rindex
28 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/multiarch/strspn.c
fn=strspn
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/strcmp.S
fn=strcmp
144 186 1 1 0 0 0 0 0 0
145 186 0 0 0 0 0 0 0 0
147 186 0 0 0 0 0 0 0 0
148 186 0 0 0 0 0 0 0 0
169 186 0 0 0 0 0 0 0 0
170 186 0 0 0 0 0 0 0 0
171 110 0 0 0 0 0 0 0 0
172 110 0 0 0 0 0 0 0 0
173 97 0 0 97 13 9 0 0 0
174 97 0 0 97 9 1 0 0 0
175 97 0 0 97 0 0 0 0 0
176 97 0 0 97 0 0 0 0 0
197 97 0 0 0 0 0 0 0 0
198 97 0 0 0 0 0 0 0 0
199 97 0 0 0 0 0 0 0 0
200 97 0 0 0 0 0 0 0 0
201 97 0 0 0 0 0 0 0 0
202 97 0 0 0 0 0 0 0 0
203 97 0 0 0 0 0 0 0 0
208 5 0 0 0 0 0 0 0 0
209 5 0 0 0 0 0 0 0 0
218 94 1 1 0 0 0 0 0 0
219 94 0 0 0 0 0 0 0 0
220 94 0 0 0 0 0 0 0 0
221 94 0 0 0 0 0 0 0 0
222 94 0 0 0 0 0 0 0 0
223 94 0 0 0 0 0 0 0 0
224 94 0 0 0 0 0 0 0 0
225 94 0 0 0 0 0 0 0 0
226 31 0 0 0 0 0 0 0 0
227 19 0 0 0 0 0 0 0 0
228 19 0 0 0 0 0 0 0 0
229 19 0 0 0 0 0 0 0 0
231 31 0 0 0 0 0 0 0 0
232 31 0 0 0 0 0 0 0 0
233 31 1 1 0 0 0 0 0 0
234 31 0 0 31 4 2 0 0 0
235 31 0 0 0 0 0 0 0 0
236 31 0 0 0 0 0 0 0 0
246 63 0 0 63 1 0 0 0 0
247 63 0 0 0 0 0 0 0 0
248 63 0 0 0 0 0 0 0 0
250 63 0 0 63 0 0 0 0 0
256 63 0 0 0 0 0 0 0 0
257 63 0 0 0 0 0 0 0 0
258 63 0 0 0 0 0 0 0 0
259 63 0 0 0 0 0 0 0 0
260 63 0 0 0 0 0 0 0 0
265 63 0 0 0 0 0 0 0 0
267 63 0 0 0 0 0 0 0 0
268 63 1 1 0 0 0 0 0 0
269 126 0 0 0 0 0 0 0 0
277 63 0 0 63 1 0 0 0 0
278 63 0 0 63 0 0 0 0 0
281 63 0 0 0 0 0 0 0 0
282 63 0 0 0 0 0 0 0 0
283 63 0 0 0 0 0 0 0 0
284 63 0 0 0 0 0 0 0 0
285 63 0 0 0 0 0 0 0 0
286 63 0 0 0 0 0 0 0 0
946 2 1 1 0 0 0 0 0 0
947 2 0 0 2 0 0 0 0 0
948 2 0 0 2 0 0 0 0 0
949 2 0 0 0 0 0 0 0 0
950 2 1 1 0 0 0 0 0 0
952 2 0 0 0 0 0 0 0 0
953 2 0 0 0 0 0 0 0 0
954 2 0 0 0 0 0 0 0 0
955 2 0 0 0 0 0 0 0 0
956 2 0 0 0 0 0 0 0 0
957 2 0 0 0 0 0 0 0 0
958 2 0 0 0 0 0 0 0 0
959 1 0 0 1 0 0 0 0 0
963 1 0 0 0 0 0 0 0 0
964 1 0 0 0 0 0 0 0 0
965 1 0 0 0 0 0 0 0 0
971 1 0 0 0 0 0 0 0 0
972 1 0 0 0 0 0 0 0 0
973 2 1 1 0 0 0 0 0 0
977 1 0 0 0 0 0 0 0 0
978 1 0 0 0 0 0 0 0 0
981 1 0 0 1 0 0 0 0 0
982 1 0 0 1 1 1 0 0 0
983 1 0 0 0 0 0 0 0 0
986 1 0 0 0 0 0 0 0 0
987 1 0 0 0 0 0 0 0 0
988 1 0 0 0 0 0 0 0 0
994 1 0 0 0 0 0 0 0 0
995 1 0 0 0 0 0 0 0 0
996 1 1 1 0 0 0 0 0 0
997 1 0 0 0 0 0 0 0 0
998 1 0 0 0 0 0 0 0 0
999 1 0 0 0 0 0 0 0 0
1071 4 1 1 0 0 0 0 0 0
1072 4 0 0 4 0 0 0 0 0
1073 4 0 0 4 0 0 0 0 0
1074 4 0 0 0 0 0 0 0 0
1075 4 1 1 0 0 0 0 0 0
1077 4 0 0 0 0 0 0 0 0
1078 4 0 0 0 0 0 0 0 0
1079 4 0 0 0 0 0 0 0 0
1080 4 0 0 0 0 0 0 0 0
1081 4 0 0 0 0 0 0 0 0
1082 4 0 0 0 0 0 0 0 0
1083 4 0 0 0 0 0 0 0 0
1084 1 0 0 1 0 0 0 0 0
1088 1 0 0 0 0 0 0 0 0
1089 1 0 0 0 0 0 0 0 0
1090 1 0 0 0 0 0 0 0 0
1096 1 0 0 0 0 0 0 0 0
1097 1 0 0 0 0 0 0 0 0
1098 2 1 1 0 0 0 0 0 0
1102 1 0 0 0 0 0 0 0 0
1103 1 0 0 0 0 0 0 0 0
1106 1 0 0 1 0 0 0 0 0
1107 1 0 0 1 0 0 0 0 0
1108 1 0 0 0 0 0 0 0 0
1111 1 0 0 0 0 0 0 0 0
1112 1 0 0 0 0 0 0 0 0
1113 1 0 0 0 0 0 0 0 0
1119 1 0 0 0 0 0 0 0 0
1120 1 0 0 0 0 0 0 0 0
1121 1 1 1 0 0 0 0 0 0
1122 1 0 0 0 0 0 0 0 0
1123 1 0 0 0 0 0 0 0 0
1124 1 0 0 0 0 0 0 0 0
1196 3 2 1 0 0 0 0 0 0
1197 3 0 0 3 1 1 0 0 0
1198 3 0 0 3 0 0 0 0 0
1199 3 0 0 0 0 0 0 0 0
1200 3 2 1 0 0 0 0 0 0
1202 3 0 0 0 0 0 0 0 0
1203 3 0 0 0 0 0 0 0 0
1204 3 0 0 0 0 0 0 0 0
1205 3 0 0 0 0 0 0 0 0
1206 3 0 0 0 0 0 0 0 0
1207 3 0 0 0 0 0 0 0 0
1208 3 0 0 0 0 0 0 0 0
1209 1 0 0 1 0 0 0 0 0
1213 1 0 0 0 0 0 0 0 0
1214 1 0 0 0 0 0 0 0 0
1215 1 0 0 0 0 0 0 0 0
1221 1 0 0 0 0 0 0 0 0
1222 1 0 0 0 0 0 0 0 0
1223 2 1 1 0 0 0 0 0 0
1227 1 0 0 0 0 0 0 0 0
1228 1 0 0 0 0 0 0 0 0
1231 1 0 0 1 0 0 0 0 0
1232 1 0 0 1 0 0 0 0 0
1233 1 0 0 0 0 0 0 0 0
1236 1 0 0 0 0 0 0 0 0
1237 1 0 0 0 0 0 0 0 0
1238 1 0 0 0 0 0 0 0 0
1244 1 0 0 0 0 0 0 0 0
1245 1 0 0 0 0 0 0 0 0
1246 1 1 1 0 0 0 0 0 0
1247 1 0 0 0 0 0 0 0 0
1248 1 0 0 0 0 0 0 0 0
1249 1 0 0 0 0 0 0 0 0
1321 3 1 1 0 0 0 0 0 0
1322 3 0 0 3 1 1 0 0 0
1323 3 0 0 3 0 0 0 0 0
1324 3 0 0 0 0 0 0 0 0
1325 3 1 1 0 0 0 0 0 0
1327 3 0 0 0 0 0 0 0 0
1328 3 0 0 0 0 0 0 0 0
1329 3 0 0 0 0 0 0 0 0
1330 3 0 0 0 0 0 0 0 0
1331 3 0 0 0 0 0 0 0 0
1332 3 0 0 0 0 0 0 0 0
1333 3 0 0 0 0 0 0 0 0
1446 4 1 1 0 0 0 0 0 0
1447 4 0 0 4 1 1 0 0 0
1448 4 0 0 4 0 0 0 0 0
1449 4 0 0 0 0 0 0 0 0
1450 4 1 1 0 0 0 0 0 0
1452 4 0 0 0 0 0 0 0 0
1453 4 0 0 0 0 0 0 0 0
1454 4 0 0 0 0 0 0 0 0
1455 4 0 0 0 0 0 0 0 0
1456 4 0 0 0 0 0 0 0 0
1457 4 0 0 0 0 0 0 0 0
1458 4 0 0 0 0 0 0 0 0
1459 4 0 0 4 0 0 0 0 0
1463 4 0 0 0 0 0 0 0 0
1464 4 0 0 0 0 0 0 0 0
1465 4 0 0 0 0 0 0 0 0
1471 4 0 0 0 0 0 0 0 0
1472 4 0 0 0 0 0 0 0 0
1473 8 1 1 0 0 0 0 0 0
1477 4 0 0 0 0 0 0 0 0
1478 4 0 0 0 0 0 0 0 0
1481 4 0 0 4 0 0 0 0 0
1482 4 0 0 4 0 0 0 0 0
1483 4 0 0 0 0 0 0 0 0
1486 4 0 0 0 0 0 0 0 0
1487 4 0 0 0 0 0 0 0 0
1488 4 0 0 0 0 0 0 0 0
1494 4 0 0 0 0 0 0 0 0
1495 4 0 0 0 0 0 0 0 0
1496 4 1 1 0 0 0 0 0 0
1497 4 0 0 0 0 0 0 0 0
1498 4 0 0 0 0 0 0 0 0
1499 4 0 0 0 0 0 0 0 0
1696 2 1 1 0 0 0 0 0 0
1697 2 0 0 2 0 0 0 0 0
1698 2 0 0 2 1 1 0 0 0
1699 2 0 0 0 0 0 0 0 0
1700 2 1 1 0 0 0 0 0 0
1702 2 0 0 0 0 0 0 0 0
1703 2 0 0 0 0 0 0 0 0
1704 2 0 0 0 0 0 0 0 0
1705 2 0 0 0 0 0 0 0 0
1706 2 0 0 0 0 0 0 0 0
1707 2 0 0 0 0 0 0 0 0
1708 2 0 0 0 0 0 0 0 0
1709 2 0 0 2 0 0 0 0 0
1713 2 0 0 0 0 0 0 0 0
1714 2 0 0 0 0 0 0 0 0
1715 2 0 0 0 0 0 0 0 0
1721 2 0 0 0 0 0 0 0 0
1722 2 0 0 0 0 0 0 0 0
1723 4 1 1 0 0 0 0 0 0
1727 2 0 0 0 0 0 0 0 0
1728 2 0 0 0 0 0 0 0 0
1731 2 0 0 2 2 2 0 0 0
1732 2 0 0 2 0 0 0 0 0
1733 2 0 0 0 0 0 0 0 0
1736 2 0 0 0 0 0 0 0 0
1737 2 0 0 0 0 0 0 0 0
1738 2 0 0 0 0 0 0 0 0
1744 2 0 0 0 0 0 0 0 0
1745 2 0 0 0 0 0 0 0 0
1746 2 1 1 0 0 0 0 0 0
1747 2 0 0 0 0 0 0 0 0
1748 2 0 0 0 0 0 0 0 0
1749 2 0 0 0 0 0 0 0 0
1756 1 0 0 0 0 0 0 0 0
1757 1 0 0 0 0 0 0 0 0
1759 1 0 0 0 0 0 0 0 0
1760 1 0 0 0 0 0 0 0 0
1762 1 0 0 1 0 0 0 0 0
1763 1 0 0 1 0 0 0 0 0
1764 1 0 0 0 0 0 0 0 0
1767 1 0 0 0 0 0 0 0 0
1768 1 0 0 0 0 0 0 0 0
1769 1 0 0 0 0 0 0 0 0
1775 1 0 0 0 0 0 0 0 0
1776 1 1 1 0 0 0 0 0 0
1777 1 0 0 0 0 0 0 0 0
1778 1 0 0 0 0 0 0 0 0
1779 1 0 0 0 0 0 0 0 0
1780 1 0 0 0 0 0 0 0 0
1821 5 1 1 0 0 0 0 0 0
1822 5 0 0 5 0 0 0 0 0
1823 5 0 0 5 1 1 0 0 0
1824 5 0 0 0 0 0 0 0 0
1825 5 1 1 0 0 0 0 0 0
1827 5 0 0 0 0 0 0 0 0
1828 5 0 0 0 0 0 0 0 0
1829 5 0 0 0 0 0 0 0 0
1830 5 0 0 0 0 0 0 0 0
1831 5 0 0 0 0 0 0 0 0
1832 5 0 0 0 0 0 0 0 0
1833 5 0 0 0 0 0 0 0 0
1834 5 0 0 5 0 0 0 0 0
1838 5 0 0 0 0 0 0 0 0
1839 5 0 0 0 0 0 0 0 0
1840 5 0 0 0 0 0 0 0 0
1846 5 0 0 0 0 0 0 0 0
1847 5 0 0 0 0 0 0 0 0
1848 10 1 1 0 0 0 0 0 0
1852 5 0 0 0 0 0 0 0 0
1853 5 0 0 0 0 0 0 0 0
1856 5 0 0 5 1 1 0 0 0
1857 5 0 0 5 0 0 0 0 0
1858 5 0 0 0 0 0 0 0 0
1861 5 0 0 0 0 0 0 0 0
1862 5 0 0 0 0 0 0 0 0
1863 5 0 0 0 0 0 0 0 0
1869 5 0 0 0 0 0 0 0 0
1870 5 0 0 0 0 0 0 0 0
1871 5 1 1 0 0 0 0 0 0
1872 5 0 0 0 0 0 0 0 0
1873 5 0 0 0 0 0 0 0 0
1874 5 0 0 0 0 0 0 0 0
1946 6 1 1 0 0 0 0 0 0
1947 6 0 0 6 0 0 0 0 0
1948 6 0 0 6 0 0 0 0 0
1949 6 0 0 0 0 0 0 0 0
1950 6 1 1 0 0 0 0 0 0
1952 6 0 0 0 0 0 0 0 0
1953 6 0 0 0 0 0 0 0 0
1954 6 0 0 0 0 0 0 0 0
1955 6 0 0 0 0 0 0 0 0
1956 6 0 0 0 0 0 0 0 0
1957 6 0 0 0 0 0 0 0 0
1958 6 0 0 0 0 0 0 0 0
1959 2 0 0 2 0 0 0 0 0
1963 2 0 0 0 0 0 0 0 0
1964 2 0 0 0 0 0 0 0 0
1965 2 0 0 0 0 0 0 0 0
1971 2 0 0 0 0 0 0 0 0
1972 2 0 0 0 0 0 0 0 0
1973 4 1 1 0 0 0 0 0 0
1977 2 0 0 0 0 0 0 0 0
1978 2 0 0 0 0 0 0 0 0
1981 2 0 0 2 1 1 0 0 0
1982 2 0 0 2 0 0 0 0 0
1983 2 0 0 0 0 0 0 0 0
1986 2 0 0 0 0 0 0 0 0
1987 2 0 0 0 0 0 0 0 0
1988 2 0 0 0 0 0 0 0 0
1994 2 0 0 0 0 0 0 0 0
1995 2 0 0 0 0 0 0 0 0
1996 2 1 1 0 0 0 0 0 0
1997 2 0 0 0 0 0 0 0 0
1998 2 0 0 0 0 0 0 0 0
1999 2 0 0 0 0 0 0 0 0
2071 2 1 1 0 0 0 0 0 0
2072 2 0 0 2 1 1 0 0 0
2073 2 0 0 2 0 0 0 0 0
2074 2 0 0 0 0 0 0 0 0
2075 2 1 1 0 0 0 0 0 0
2077 2 0 0 0 0 0 0 0 0
2078 2 0 0 0 0 0 0 0 0
2079 2 0 0 0 0 0 0 0 0
2080 2 0 0 0 0 0 0 0 0
2081 2 0 0 0 0 0 0 0 0
2082 2 0 0 0 0 0 0 0 0
2083 2 0 0 0 0 0 0 0 0
2200 79 0 0 0 0 0 0 0 0
2202 94 1 1 0 0 0 0 0 0
2203 94 0 0 0 0 0 0 0 0
2204 94 0 0 0 0 0 0 0 0
2205 94 1 1 0 0 0 0 0 0
2206 57 0 0 0 0 0 0 0 0
2211 186 0 0 0 0 0 0 0 0
2217 186 0 0 186 0 0 0 0 0
2218 186 0 0 186 0 0 0 0 0
2226 186 0 0 0 0 0 0 0 0
2227 186 0 0 186 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/../sysdeps/x86_64/strcspn.S
fn=strcspn
30 1 1 1 0 0 0 0 0 0
37 1 0 0 0 0 0 0 0 0
38 1 0 0 0 0 0 0 0 0
40 1 0 0 0 0 0 0 0 0
41 1 0 0 0 0 0 0 0 0
42 1 0 0 0 0 0 0 0 0
43 1 0 0 0 0 0 0 0 0
44 33 0 0 0 0 0 32 4 4
47 2 0 0 0 0 0 0 0 0
54 1 0 0 1 0 0 0 0 0
55 1 0 0 0 0 0 0 0 0
56 1 0 0 0 0 0 0 0 0
57 1 0 0 0 0 0 1 0 0
59 1 0 0 1 0 0 0 0 0
60 1 0 0 0 0 0 0 0 0
61 1 0 0 0 0 0 0 0 0
62 1 0 0 0 0 0 1 0 0
64 1 0 0 1 0 0 0 0 0
65 1 0 0 0 0 0 0 0 0
66 1 0 0 0 0 0 0 0 0
75 3 1 1 0 0 0 0 0 0
87 12 0 0 0 0 0 0 0 0
89 12 0 0 12 1 1 0 0 0
90 12 0 0 12 0 0 0 0 0
91 12 0 0 0 0 0 0 0 0
93 12 0 0 12 0 0 0 0 0
94 12 0 0 12 0 0 0 0 0
95 12 0 0 0 0 0 0 0 0
97 12 0 0 12 0 0 0 0 0
98 12 0 0 12 0 0 0 0 0
99 12 0 0 0 0 0 0 0 0
101 12 0 0 12 0 0 0 0 0
102 12 0 0 12 0 0 0 0 0
103 12 0 0 0 0 0 0 0 0
105 1 0 0 0 0 0 0 0 0
106 1 0 0 0 0 0 0 0 0
107 1 0 0 0 0 0 0 0 0
109 1 0 0 0 0 0 0 0 0
116 1 0 0 0 0 0 0 0 0
120 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/string/strdup.c
fn=strdup
40 12 1 1 0 0 0 6 0 0
41 6 1 1 0 0 0 3 0 0
42 6 0 0 0 0 0 3 0 0
44 6 0 0 0 0 0 0 0 0
47 12 0 0 0 0 0 0 0 0
48 9 0 0 6 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/time/../sysdeps/generic/dl-hash.h
fn=gettimeofday
43 1 0 0 0 0 0 0 0 0
44 1 1 1 0 0 0 0 0 0
45 13 1 1 4 0 0 0 0 0
48 12 0 0 0 0 0 0 0 0
62 16 0 0 0 0 0 0 0 0
67 1 0 0 0 0 0 0 0 0
fn=time
44 1 0 0 0 0 0 0 0 0
45 13 0 0 4 1 1 0 0 0
48 12 1 1 0 0 0 0 0 0
62 16 0 0 0 0 0 0 0 0
67 1 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/time/../sysdeps/unix/sysv/linux/x86/gettimeofday.c
fn=gettimeofday
42 16 1 1 1 0 0 4 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/time/../sysdeps/unix/sysv/linux/x86/time.c
fn=time
43 17 2 2 1 0 0 4 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/ifunc-avx2.h
fn=wcschr
30 8 0 0 0 0 0 0 0 0
32 6 1 1 4 0 0 0 0 0
fn=wcslen
30 4 0 0 0 0 0 0 0 0
32 3 1 1 2 0 0 0 0 0
fn=wmemchr
30 8 0 0 0 0 0 0 0 0
32 6 2 2 4 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/ifunc-wmemset.h
fn=wmemset
30 6 1 1 0 0 0 0 0 0
32 8 1 1 4 0 0 0 0 0
34 8 0 0 0 0 0 0 0 0
35 2 0 0 0 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wcschr.c
fn=wcschr
31 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wcslen.c
fn=wcslen
29 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wcsnlen.c
fn=wcsnlen
38 3 1 1 0 0 0 0 0 0
40 3 1 1 2 0 0 0 0 0
49 1 0 0 1 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wmemchr.c
fn=wmemchr
31 2 0 0 2 0 0 0 0 0
fl=/build/glibc-S9d2JN/glibc-2.27/wcsmbs/../sysdeps/x86_64/multiarch/wmemset.c
fn=wmemset
31 2 0 0 2 0 0 0 0 0
fl=???
fn=???
0 2051 28 21 1965 7 0 21 1 1
fn=FindPrimes
0 32968 2 2 13657 2 0 5105 36 35
fn=ShowProgress
0 76995 1 1 16199 1 1 12199 0 0
fn=TestForPrime
0 7258430 1 1 2589625 0 0 9450 0 0
fn=__libc_csu_init
0 34 2 2 8 0 0 8 0 0
fn=_start
0 11 1 1 2 0 0 3 0 0
fn=main
0 1317 2 2 506 1 0 104 0 0
summary: 7805391 1122 1093 2724178 2519 2052 75847 706 622
desc: (none)
cmd: ./prime-ex
time_unit: i
#-----------
snapshot=0
#-----------
time=0
mem_heap_B=0
mem_heap_extra_B=0
mem_stacks_B=0
heap_tree=empty
#-----------
snapshot=1
#-----------
time=132973
mem_heap_B=1024
mem_heap_extra_B=8
mem_stacks_B=0
heap_tree=empty
#-----------
snapshot=2
#-----------
time=7754891
mem_heap_B=1024
mem_heap_extra_B=8
mem_stacks_B=0
heap_tree=peak
n1: 1024 (heap allocation functions) malloc/new/new[], --alloc-fns, etc.
 n1: 1024 0x4EB326A: _IO_file_doallocate (filedoalloc.c:101)
  n1: 1024 0x4EC3447: _IO_doallocbuf (genops.c:365)
   n1: 1024 0x4EC2566: _IO_file_overflow@@GLIBC_2.2.5 (fileops.c:759)
    n1: 1024 0x4EC0ABB: _IO_file_xsputn@@GLIBC_2.2.5 (fileops.c:1266)
     n1: 1024 0x4E90632: vfprintf (vfprintf.c:1328)
      n1: 1024 0x4E9A014: printf (printf.c:33)
       n1: 1024 0x108722: ShowProgress (in /home/student/Documents/ASC/lab6/prime-ex)
        n1: 1024 0x108790: FindPrimes (in /home/student/Documents/ASC/lab6/prime-ex)
         n0: 1024 0x1087C3: main (in /home/student/Documents/ASC/lab6/prime-ex)
#-----------
snapshot=3
#-----------
time=7754891
mem_heap_B=0
mem_heap_extra_B=0
mem_stacks_B=0
heap_tree=empty
