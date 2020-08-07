@echo off

set ANACONDA_HOME=%HOMEPATH%\anaconda3
call %ANACONDA_HOME%\Scripts\activate.bat dric
%ANACONDA_HOME%\envs\dric\python dric_camera_agent.py %*