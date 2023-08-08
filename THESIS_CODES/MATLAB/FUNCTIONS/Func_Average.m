%%SIGNAL AVERAGING FUNCTION
%DataIn - Input matrix whit signals
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Average(DataIn)

    DataOut = mean(DataIn,2);
    
end