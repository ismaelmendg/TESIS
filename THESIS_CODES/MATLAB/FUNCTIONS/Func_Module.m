%%FUNCTION TO GET THE MACHINE LEARNING MODEL
%model - Machine learning model 
%DataIn - Data matrix
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Module(model, DataIn)

    [~, B] = size(DataIn);
    
    if model == "fitcnb"
        DataOut = fitcnb(DataIn(:, 1:B-1), DataIn(:,B));
    elseif model == "fitcecoc"
        DataOut = fitcecoc(DataIn(:, 1:B-1), DataIn(:,B));
    elseif model == "fitctree"
        DataOut = fitctree(DataIn(:, 1:B-1), DataIn(:,B));
    elseif model == "fitcknn"
        DataOut = fitcknn(DataIn(:, 1:B-1), DataIn(:,B));
    elseif model == "fitcdiscrq"
        DataOut = fitcdiscr(DataIn(:, 1:B-1), DataIn(:,B),'DiscrimType','quadratic');
    else 
        DataOut = fitcdiscr(DataIn(:, 1:B-1), DataIn(:,B));
    end    

end