%%High PASS FILTER FUNCITON
% Returns the parameter for the filter required
% fc - Is equla to the cut frecuency
% fs - Is equla to the frecuency sample 
% order - Is the order for the filter
% column - column number containing the needed data

% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_HPF(fc, fs, order, DataIn, column)

    [b, a] = butter(order, fc/(fs/2), 'High');
    DataOut = filter(b, a, DataIn(:,column));
    
end