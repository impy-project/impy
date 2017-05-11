      SUBROUTINE SIGMA_NUC_AIR(IA,ECM,NINT)
      IMPLICIT REAL(A-H,O-Z)
C.  wrapping for SIGMA_NUC in NUCLIB
C...Compute with a montecarlo method the "production"
C.  and "quasi-elastic" cross section for  
C.  a nucleus-nucleus interaction
C.  nucleon - nucleon cross section is taken from 
C.  the table calculated by SIBYLL_INI
C.
C.  INPUT : IA            = mass of target nucleus
C.          ECM          = c.m. energy
C.          NINT            = number  of interactions to generate
C.  OUTPUT : SIGMA (mbarn) = "production" cross section
C.           DSIGMA   "    = error
C.           SIGQE    "    = "quasi-elastic" cross section
C.           DSIGQE   "    = error
C.      in COMMON /NUCNUCSIG/ 
C.           additional output is in the common block  /CPROBAB/
C.           Prob(n_A), Prob(n_B), Prob(n_int)
C..........................................................................
      SAVE
      COMMON /NUCNUCSIG/ IBE,ITG,SIGPROD,DSIGPROD,SIGQE,DSIGQE
      DIMENSION SIGDIF(3)

      DSIGPROD = 0.
      DSIGQE = 0.

      CALL SIB_SIGMA_HP(1,ECM,SIGT,SIGEL,SIGINEL,SIGDIF,SLOPE,RHO)
      CALL SIGMA_AIR(IA,SIGINEL,SIGEL,NINT,SIGPROD,DSIGPROD,
     +     SIGQE,DSIGQE)
      IBE = IA
      ITG = 0
      IF(DSIGPROD/SIGPROD.gt.0.1)THEN
         IF( NDB.EQ.0 ) 
     +     PRINT*,'SIG_NUC_AIR: warning! : large error in cross section'
         NDB = 1
      ENDIF
      RETURN
      END


      SUBROUTINE SIG_NUC_AIR(IA,SIGPP,SIGPPEL,NINT)
      IMPLICIT REAL(A-H,O-Z)
C.  wrapping for SIGMA_NUC in NUCLIB
C...Compute with a montecarlo method the "production"
C.  and "quasi-elastic" cross section for  
C.  a nucleus-nucleus interaction
C.
C.  INPUT : IA            = mass of target nucleus
C.          IB            = mass of projectile nucleus
C.          SIGPP (mbarn)  = inelastic pp cross section
C.          SIGPPEL        = elastic pp cross section
C.          NINT            = number  of interactions to generate
C.  OUTPUT : SIGMA (mbarn) = "production" cross section
C.           DSIGMA   "    = error
C.           SIGQE    "    = "quasi-elastic" cross section
C.           DSIGQE   "    = error
C.      in COMMON /NUCNUCSIG/ 
C.           additional output is in the common block  /CPROBAB/
C.           Prob(n_A), Prob(n_B), Prob(n_int)
C..........................................................................
      SAVE
      COMMON /NUCNUCSIG/ IBE,ITG,SIGPROD,DSIGPROD,SIGQE,DSIGQE
      DSIGPROD = 0.
      DSIGQE = 0.
      CALL SIGMA_AIR(IA,SIGPP,SIGPPEL,NINT,SIGPROD,DSIGPROD,
     +     SIGQE,DSIGQE)
      IBE = IA
      ITG = 0
      IF(DSIGPROD/SIGPROD.gt.0.1)THEN
         IF( NDB.EQ.0 ) 
     +     PRINT*,'SIG_NUC_AIR: warning! : large error in cross section'
         NDB = 1
      ENDIF
      RETURN
      END


      SUBROUTINE SIG_NUC_NUC(IA,IB,SIGPP,SIGPPEL,NINT)
      IMPLICIT REAL(A-H,O-Z)
C.  wrapping for SIGMA_NUC in NUCLIB
C...Compute with a montecarlo method the "production"
C.  and "quasi-elastic" cross section for  
C.  a nucleus-nucleus interaction
C.
C.  INPUT : IA            = mass of target nucleus
C.          IB            = mass of projectile nucleus
C.          SIGPP (mbarn)  = inelastic pp cross section
C.          SIGPPEL        = elastic pp cross section
C.          NINT            = number  of interactions to generate
C.  OUTPUT : SIGMA (mbarn) = "production" cross section
C.           DSIGMA   "    = error
C.           SIGQE    "    = "quasi-elastic" cross section
C.           DSIGQE   "    = error
C.      in COMMON /NUCNUCSIG/ 
C.           additional output is in the common block  /CPROBAB/
C.           Prob(n_A), Prob(n_B), Prob(n_int)
C..........................................................................
      SAVE
      COMMON /NUCNUCSIG/ IBE,ITG,SIGPROD,DSIGPROD,SIGQE,DSIGQE
      DSIGPROD = 0.
      DSIGQE = 0.
      CALL SIGMA_MC(IA,IB,SIGPP,SIGPPEL,NINT,SIGPROD,DSIGPROD,
     +     SIGQE,DSIGQE)
      IBE = IA
      ITG = IB
      IF(DSIGPROD/SIGPROD.gt.0.1)THEN
         IF( NDB.EQ.0 ) 
     +     PRINT*,'SIG_NUC_NUC: warning! : large error in cross section'
         NDB = 1
      ENDIF
      RETURN
      END

      SUBROUTINE SIG_HAD_NUC(L,IA,ECM,ALAM,ICSMOD,IPARM)
C**********************************************************************
C...Subroutine to compute hadron-nucleus cross sections
C.  according to:
C.  R.J. Glauber and G.Matthiae  Nucl.Phys. B21, 135, (1970)
C.
C.
C.  INPUT :  L projectile particle (1:p , 2:pi, 3:K )
C.           IA mass-number of target nucleus
C.           SSIG  (mbarn) total pp cross section
C.           SLOPE (GeV**-2)  elastic scattering slope for pp
C.           ALPHA    real/imaginary part of the forward pp elastic
C.                                               scattering amplitude
C.           ALAM: inel. screening coupling
C.
C.  OUTPUT : ( in COMMON block /NUCSIG/ )
C.           SIGT  = Total cross section
C.           SIGEL = Elastic cross section
C.           SIGQEL  = Elastic + Quasi elastic cross section
C.           SIGSD  = beam single diff. cross section
C......................................................................
      SAVE
      COMMON /NUCSIG/ ITG,SIGT,SIGEL,SIGINEL,SIGQE,SIGSD,
     +     SIGPPT,SIGPPEL,SIGPPSD
      dimension ssigdif(3),XM(4)     
      DATA XM / 0.93956563, 0.13956995, 0.493677, 0.93956563 /
      data PI /3.1415926/
      data GEV2MB /0.3893/
      double precision dplab
      double precision DSSIG,DSLOPE,DALPHA,DALAM
      DOUBLE PRECISION SG1,SGEL1,SGQE1,SGSD1,SGQSD1
      xma = XM(L)
      xmb = (XM(1)+XM(4))/2.D0

      dPlab = sqrt(((ecm**2-xma**2-xmb**2)/(2.D0*xmb))**2-xma**2)
      plab = dplab


C     hadron proton cross section to be used for calculation

      IF( ICSMOD.EQ.1 ) THEN
c     sibyll 2.1 cross section

         CALL SIB_SIGMA_HP(L,ECM,SSIG,SSIGEL,SSIGINEL,SSIGDIF,SLOPE,RHO) 

      ELSEIF( ICSMOD.EQ.0 ) THEN
c     cross section parametrizations

         if(Ecm.gt.12.0) then

           call SIB_HADCSL(L,ECM,SSIG,SSIGEL,SSIGINEL,SSIGDIF,SLOPE,RHO)

         else
c     low energy parametrization
            SSIG = (sigtot_pp(dPlab)+sigtot_pn(dplab))/2.D0
            SSIGEL  = (sigela_pp(dPlab)+sigela_pn(dplab))/2.D0
C     parametrization from U. Dersch et al. Nucl Phys. B579 (2000) 277
            RHO = 6.8D0/plab**0.742D0-6.6D0/plab**0.599+0.124
            SLOPE = (1.D0+RHO**2)*SIGTOT**2/(16.D0*PI*SIGEL)/GEV2MB
            SSIGDIF(1) = 0.D0
            SSIGDIF(2) = 0.D0
            SSIGDIF(3) = 0.D0
         endif
      ENDIF
      SSIGSD = SSIGDIF(1) + SSIGDIF(2)

c     energy dependence of lambda parameter
      if( IPARM.eq.1 ) then

c     empirical parametrization
         SIGEFF = 0.25D0*Ecm**2/(Ecm**2+10.D0**2)*LOG(1000.D0*Ecm**2)
     &        -1.5D0/2.D0
         SIGEFF = MAX(0.,SIGEFF)
         
         ALAM = sqrt(SIGEFF/SSIGEL)

         SSIGSD = 2. * SIGEFF
      elseif( IPARM.EQ.2 ) then

C  parametrization by Goulianos
         SIGEFF = 0.68D0*(1.D0+36.D0/Ecm**2)
     &        *LOG(0.6D0+0.02D0/1.5D0*Ecm**2)
         SIGEFF = MAX(0.,SIGEFF)
         ALAM = sqrt(SIGEFF/SSIGEL)
         
         SSIGSD = 2. * SIGEFF
      elseif( IPARM.eq.3)then

C     data from Paolo Lipari's note
         SIGTOT = 129.D0
         SIGEL  = 0.3*SIGTOT
         SIGEFF = ECM*0.01*SIGTOT
         RHO    = 0.D0
         SLOPE  = (1.D0+RHO**2)*SIGTOT**2/(16.D0*PI*SIGEL)/GEV2MB
         ALAM   = sqrt(SIGEFF/SIGEL)
         
         SSIG = SIGTOT
         SSIGEL = SIGEL
         SSIGSD = 2. * SIGEFF
      endif 

      ALPHA = RHO

c      print*,ssig,ssigel,slope,alpha,alam

C     hadron - nucleon cross section
      
      IF( IA.EQ.0 ) THEN
         call SIG_H_AIR2
     +        (SSIG,SLOPE,ALPHA,ALAM,SIG1,SIGEL1,SIGQE1,SIGSD1,SIGQSD1)
      else
         if( ALAM.eq.0. ) then
            CALL GLAUBER(IA,SIG1,SLOPE,ALPHA,SIG1,SIGEL1,SIGQE1)
         else
            DSSIG = SSIG
            DSLOPE = SLOPE
            DALPHA = ALPHA
            DALAM = ALAM
            CALL GLAUBER2
     +  (IA,DSSIG,DSLOPE,DALPHA,DALAM,SG1,SGEL1,SGQE1,SGSD1,SGQSD1)
         endif
      endif

      ITG = IA

      SIGPPT = SSIG
      SIGPPEL = SSIGEL
      SIGPPSD = SSIGSD
      SIGT  = SIG1
      SIGEL = SIGEL1
      SIGQE = SIGQE1
      SIGSD = SIGSD1
      SIGQSD = SIGQSD1
      SIGINEL = SIGT - SIGEL

      RETURN
      END

      SUBROUTINE SIG_H_AIR2
     +     (SSIG,SLOPE,ALPHA,ALAM,SIGT,SIGEL,SIGQE,SIGSD,SIGQSD)
C**********************************************************************
C...Subroutine to compute hadron-air cross sections
C.  according to:
C.  R.J. Glauber and G.Matthiae  Nucl.Phys. B21, 135, (1970)
C.
C.  Air is a linear combination of Nitrogen and oxygen
C.
C.  INPUT :  SSIG  (mbarn) total pp cross section
C.           SLOPE (GeV**-2)  elastic scattering slope for pp
C.           ALPHA    real/imaginary part of the forward pp elastic
C.                                               scattering amplitude
C.  OUTPUT : SIGT  = Total cross section
C.           SIGEL = Elastic cross section
C.           SIGQEL  = Elastic + Quasi elastic cross section
C.           SIGSD   = single diff. cross section (beam) 
C.           SIGQSD  = Elastic + Quasi elastic SD cross section (beam)
C.
C.  ALSO including interface from single precision in SIBYLL to
C.       double precision in GLAUBER2
C......................................................................
c      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      SAVE
      DATA  FOX /0.257/
      DOUBLE PRECISION DSSIG,DSLOPE,DALPHA,DALAM
      DOUBLE PRECISION SIG1,SIGEL1,SIGQE1,SIGSD1,SIGQSD1
      DOUBLE PRECISION SIG2,SIGEL2,SIGQE2,SIGSD2,SIGQSD2
      DSSIG = SSIG
      DSLOPE = SLOPE
      DALPHA = ALPHA
      DALAM = ALAM
      CALL GLAUBER2
     +  (14,DSSIG,DSLOPE,DALPHA,DALAM,SIG1,SIGEL1,SIGQE1,SIGSD1,SIGQSD1)
      CALL GLAUBER2
     +  (16,DSSIG,DSLOPE,DALPHA,DALAM,SIG2,SIGEL2,SIGQE2,SIGSD2,SIGQSD2)
      SIGT  = (1.-FOX)*SIG1   + FOX*SIG2
      SIGEL = (1.-FOX)*SIGEL1 + FOX*SIGEL2
      SIGQE = (1.-FOX)*SIGQE1 + FOX*SIGQE2
      SIGSD = (1.-FOX)*SIGSD1 + FOX*SIGSD2
      SIGQSD = (1.-FOX)*SIGQSD1 + FOX*SIGQSD2
      RETURN
      END


      SUBROUTINE GLAUBER2
     +     (JA,SSIG,SLOPE,ALPHA,ALAM,SIGT,SIGEL,SIGQEL,SIGSD,SIGQSD)
C-----------------------------------------------------------------------
C...Subroutine to compute hadron-Nucleus cross sections
C.  according to:
C.  R.J. Glauber and G.Matthiae  Nucl.Phys. B21, 135, (1970)
C.
C.  This formulas assume that the target nucleus  density is
C.  modeled by a shell-model form.  A reasonable range of models
C.  is  4 < JA < 18
C.
C.  This is a modified version with a two-channel model for inelastic
C.  intermediate states of low mass (R. Engel 2012/03/26)
C.
C.  INPUT :  A = mass number of the nucleus
C.           SSIG  (mbarn) total pp cross section
C.           SLOPE (GeV**-2)  elastic scattering slope for pp
C.           ALAM  enhancement factor (sqrt of sigma_sd1/sigma_ela)
C.           ALPHA    real/imaginary part of the forward pp elastic
C.                                               scattering amplitude
C.  OUTPUT : SIGT  = Total cross section
C.           SIGEL = Elastic cross section
C.           SIGQEL  = Elastic + Quasi elastic cross section
C.           SIGSD = single diff. cross section
C.           SIGQSD = Quasi single diff. cross section
C.
C. Internally  everything is computed in GeV (length = GeV**-1)
C-----------------------------------------------------------------------
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      COMMON /CA0SH/ R0, R02
      SAVE
      COMPLEX  ZS1, ZS2, ZP1, ZP2, Z1, Z2, OM12
      DIMENSION RR(18)

      DATA CMBARN /0.389385D0/
      DATA PI /3.1415926D0/
      DATA BMAX /100.D0/            ! GeV**-1
      DATA NB /500/
C...data on Sqrt[<r**2>] (fm). (A=5,8 are not correct).
C   From Barett and Jackson
      DATA RR /0.81,2.095,1.88,1.674, 2.56,2.56,2.41,2.5,2.519,2.45
     +          ,2.37, 2.460, 2.440, 2.54, 2.58, 2.718, 2.662,2.789 /

      A = FLOAT(JA)
C...Parameter of shell model density
      R0 = RR(JA)/0.197D0/SQRT(5.D0/2.D0 - 4.D0/A)    ! GeV**-1
      R02 = R0*R0

      SIG1 = (1.D0+ALAM) * SSIG/CMBARN            ! GeV**-2
      SIG2 = (1.D0-ALAM) * SSIG/CMBARN
      SIG12 = SQRT((1.D0+ALAM)*(1.D0-ALAM)) * SSIG/CMBARN
      DB = BMAX/FLOAT(NB)
      SUM  = 0.D0
      SUM1 = 0.D0
      SUM2 = 0.D0
      SUM3 = 0.D0
      SUM4 = 0.D0
      DO JB=1,NB

        B = DB*(FLOAT(JB)-0.5D0)

        GS1 = GLAUBGS_D (B,SLOPE, SIG1)
        XS1 = (1.D0- GS1)
        YS1 = GS1*ALPHA
        ZS1 = CMPLX(XS1,YS1)

        GP1 = GLAUBGP_D (B,SLOPE, SIG1)
        XP1 = (1.D0- GP1)
        YP1 = GP1*ALPHA
        ZP1 = CMPLX(XP1,YP1)

        Z1 = ZS1**4.D0 * ZP1**(A-4.D0)

        GS2 = GLAUBGS_D (B,SLOPE, SIG2)
        XS2 = (1.D0- GS2)
        YS2 = GS2*ALPHA
        ZS2 = CMPLX(XS2,YS2)

        GP2 = GLAUBGP_D (B,SLOPE, SIG2)
        XP2 = (1.D0- GP2)
        YP2 = GP2*ALPHA
        ZP2 = CMPLX(XP2,YP2)

        Z2 = ZS2**4.D0 * ZP2**(A-4.D0)

        XZ = 0.5D0 * REAL(Z1+Z2)
        YZ = 0.5D0 * AIMAG(Z1+Z2)

        XZ2 = 0.5D0 * REAL(Z2-Z1)
        YZ2 = 0.5D0 * AIMAG(Z2-Z1)

        SUM = SUM + (1.D0-XZ)*B

        SUM1 = SUM1 + ((1.D0-XZ)**2 + YZ**2)*B

        SUM3 = SUM3 + (XZ2**2 + YZ2**2)*B

        OMS1 = OMEGAS_D(B,SIG1,SLOPE,ALPHA)
        OMS2 = OMEGAS_D(B,SIG2,SLOPE,ALPHA)
        OMS12 = OMEGAS_D(B,SIG12,SLOPE,ALPHA)

        OMP1 = OMEGAP_D(B,SIG1,SLOPE,ALPHA)
        OMP2 = OMEGAP_D(B,SIG2,SLOPE,ALPHA)
        OMP12 = OMEGAP_D(B,SIG12,SLOPE,ALPHA)

        OM1 = (1.D0 - 2.D0*GS1 + OMS1)**4.D0
     &      * (1.D0 - 2.D0*GP1 + OMP1)**(A-4.D0)
        OM2 = (1.D0 - 2.D0*GS2 + OMS2)**4.D0
     &      * (1.D0 - 2.D0*GP2 + OMP2)**(A-4.D0)
        OM12 = (1.D0 - GS1*CMPLX(1.D0,ALPHA) - GS2*CMPLX(1.D0,-ALPHA)
     &               + OMS12)**4.D0
     &       * (1.D0 - GP1*CMPLX(1.D0,ALPHA) - GP2*CMPLX(1.D0,-ALPHA)
     &               + OMP12)**(A-4.D0)
        SUM2 = SUM2 + (1.D0-2.D0*XZ + (OM1+OM2)/4.D0
     &                 + REAL(OM12)/2.D0)*B
        SUM4 = SUM4 + ((OM1+OM2)/4.D0
     &                 - REAL(OM12)/2.D0)*B

      ENDDO

      SIGT =   SUM  * DB * 4.D0*PI * CMBARN
      SIGEL =  SUM1 * DB * 2.D0*PI * CMBARN
      SIGQEL = SUM2 * DB * 2.D0*PI * CMBARN
      SIGSD =  SUM3 * DB * 2.D0*PI * CMBARN
      SIGQSD = SUM4 * DB * 2.D0*PI * CMBARN
      END


      FUNCTION GLAUBGS_D (B,SLOPE, SIG)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      COMMON /CA0SH/ A0, A02
      SAVE
      DATA PI /3.1415926/
      GAMMA2 = A02/4. + 0.5*SLOPE
      ARG = B**2/(4.*GAMMA2)
      GLAUBGS_D = SIG/(8.*PI*GAMMA2) * EXP(-ARG)
      RETURN
      END


      FUNCTION GLAUBGP_D (B,SLOPE, SIG)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      COMMON /CA0SH/ A0, A02
      SAVE
      DATA PI /3.1415926/
      GAMMA2 = A02/4. + 0.5*SLOPE
      ARG = B**2/(4.*GAMMA2)
      C1 = 1.- A02/(6.*GAMMA2)*(1.-ARG)
      GLAUBGP_D = SIG/(8.*PI*GAMMA2) *  C1 * EXP(-ARG)
      RETURN
      END


      FUNCTION OMEGAS_D (B, SIG, SLOPE, RHO)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      COMMON /CA0SH/ A0, A02
      SAVE
      DATA PI /3.1415926/
      ETA2 = 0.25*(A02 + SLOPE)
      F02 = SIG*SIG*(1.+RHO*RHO)/(16.*PI**2)
      ARG = -B*B/(4.*ETA2)
      OMEGAS_D = F02/(4.*ETA2*SLOPE) *EXP(ARG)
      RETURN
      END


      FUNCTION OMEGAP_D (B, SIG, SLOPE, RHO)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      COMMON /CA0SH/ A0, A02
      SAVE
      DATA PI /3.1415926/
      ETA2 = 0.25*(A02 + SLOPE)
      F02 = SIG*SIG*(1.+RHO*RHO)/(16.*PI**2)
      ARG = -B*B/(4.*ETA2)
      OMEGAP_D=F02/(4.*ETA2*SLOPE)*(1.-A02/(6.*ETA2)*(1.+ARG))*EXP(ARG)
      RETURN
      END
