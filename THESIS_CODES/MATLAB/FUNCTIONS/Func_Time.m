%%TIME VECTOR FUNCTION
%Fs - sample ratr
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Time(Fs)

    T = 1/Fs;
    DataOut = (-1:T:4-T)';
    
end
